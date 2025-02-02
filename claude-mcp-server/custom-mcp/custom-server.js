       const { Server } = require("@modelcontextprotocol/sdk/server");
       const tools = {
         "python_code_execute": {
           description: "Executes Python code",
           schema: { code: { type: "string", required: true } },
           callback: async ({ code }) => {
             console.log(`Executing Python: ${code}`);
             return `Output of code '${code}'`;
           }
         },
         "git_status": {
           description: "Get Git repository status",
           schema: { repoPath: { type: "string" } },
           callback: async ({ repoPath }) => {
             return `Git status for: ${repoPath}`;
           }
         }
       };
       const startServer = async () => {
         const server = new Server({ name: "custom-mcp", version: "0.1" }, { tools });
         server.listen(3000).then(() => console.log("Custom MCP Server running on Port 3000"));
       };
       startServer().catch(console.error);