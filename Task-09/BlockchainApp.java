import org.hyperledger.fabric.gateway.*;
import java.nio.file.Path;
import java.nio.file.Paths;

public class BlockchainApp {
public static void main(String[] args)throws Exception {
PathwalletPath=Paths.get("wallet");
Walletwallet=Wallets.newFileSystemWallet(walletPath);

PathnetworkConfigPath=Paths.get("connection-org1.json");
        Gateway.Builderbuilder=Gateway.createBuilder()
                .identity(wallet, "admin")
                .networkConfig(networkConfigPath);

try (Gatewaygateway= builder.connect()) {
Networknetwork=gateway.getNetwork("mychannel");
Contractcontract=network.getContract("mycc");

// Submit a transaction
byte[] result = contract.submitTransaction("createAsset", "asset1", "value1");
System.out.println("Transaction successful: " + newString(result));

// Query the asset
byte[] queryResult = contract.evaluateTransaction("readAsset", "asset1");
System.out.println("Query Result: " + newString(queryResult));
        }
    }
}
