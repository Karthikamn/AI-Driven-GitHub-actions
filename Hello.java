public class Hello {
    public static void main(String[] args) {
        // Hardcoded AWS keys (triggers HIGH regex)
        String accessKey = "AKIA1234567890TESTKEY";
        String secretKey = "abcdabcdabcdabcdabcdabcdabcdabcdabcdddd";

        // Hardcoded password (triggers HIGH regex)
        String password = "SuperSecret1235";

        // Unsafe code (triggers LOW regex)
        eval("2 + 2");
        String apiKey = "my-secret-api-key";

        System.out.println("Hello, world!");
    }
}

