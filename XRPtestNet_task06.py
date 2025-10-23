!pip install --upgrade "httpx<1.0.0,>=0.28.1"
!pip install xrpl-py --quiet


import xrpl
import pkg_resources
print("xrpl-py:", pkg_resources.get_distribution("xrpl-py").version)

!pip -q install nest_asyncio
import nest_asyncio, asyncio
nest_asyncio.apply()

# --- XRPL v4.3.0 async example: send 1 XRP on Testnet ---

from xrpl.asyncio.clients import AsyncJsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import Payment
from xrpl.asyncio.transaction import autofill, sign, submit_and_wait
from xrpl.models.requests import AccountInfo, Tx

JSON_RPC_URL = "https://s.altnet.rippletest.net:51234"
client = AsyncJsonRpcClient(JSON_RPC_URL)

ALICE_SEED  = "sEd7enoGxfjCgSsuCdVvi7ykdZ7WcQc"       # faucet secret
BOB_ADDRESS = "rEPR7ca3uzKyGKFAbMCnncuZVmNEQsm832"     # receiver

alice = Wallet.from_seed(ALICE_SEED)

async def balance_drops(addr: str) -> int:
    req = AccountInfo(account=addr, ledger_index="validated", strict=True)
    res = await client.request(req)
    return int(res.result["account_data"]["Balance"])

print("Before  -> Alice:", await balance_drops(alice.classic_address),
      "| Bob:", await balance_drops(BOB_ADDRESS))

# Build payment
tx = Payment(
    account=alice.classic_address,
    destination=BOB_ADDRESS,
    amount="1000000"  # 1 XRP in drops
)

# Async -> autofill, sync -> sign, async -> submit_and_wait
tx = await autofill(tx, client)     # await (network call)
signed = sign(tx, alice)            # NO await (pure local signing)
final = await submit_and_wait(signed, client)  # await (network/validation)

tx_hash = signed.get_hash()
print("TX Hash:", tx_hash)


from xrpl.models.requests import Tx

# If tx_hash variable isn’t in scope, paste it:
# tx_hash = "BA000472497676B6978E7D253F82624FA9A4290513F8911A7ED155F6BF0D0411"

tx_info = (await client.request(Tx(transaction=tx_hash))).result
print("Validated:", tx_info.get("validated"))
print("Engine Result:", tx_info.get("meta", {}).get("TransactionResult"))
print("Fee (drops):", tx_info.get("Fee"))
print("Destination:", tx_info.get("Destination"))
print("Amount (drops):", tx_info.get("Amount"))


print("After -> Alice:", await balance_drops(alice.classic_address),
      "| Bob:", await balance_drops(BOB_ADDRESS))


from xrpl.models.transactions import Payment, Memo
import binascii

# Example metadata
DEST_TAG = 2025
note = "AIML Lab: XRPL payment"

# XRPL requires memo data to be hex-encoded
note_hex = binascii.hexlify(note.encode("utf-8")).decode("utf-8")

# Build Payment with memo + destination tag
tx = Payment(
    account=alice.classic_address,
    destination=BOB_ADDRESS,
    amount="1000000",        # 1 XRP
    destination_tag=DEST_TAG,
    memos=[Memo(memo_data=note_hex)],
)

# Autofill, sign, and submit
tx = await autofill(tx, client)
signed = sign(tx, alice)        # sync
final = await submit_and_wait(signed, client)

print("TX Hash (memo+tag):", signed.get_hash())
