from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<title>revenue table</title>
<body align="center" bgcolor="white">
<caption><h1>Top Five Revenue Generating Software Companies</h1></caption>
<table align="center" border ="2" cellpadding="10">
<tr>
 <th> S.No </th>
 <th> Company </th>
 <th> Revenue </th>
</tr>
<tr>
 <th> 1 </th>
 <td> Microsoft </td>
 <td> 65 Billion </td>
</tr>
<tr>
 <th> 2 </th>
 <td> Oracle </td>
 <td> 29.6 Billion </td>
</tr>
<tr>
 <th> 3</th>
 <td> IBM </td>
 <td> 29.1 Billion </td>
</tr>
<tr>
 <th> 4 </th>
 <td> SAP </td>
 <td> 6.4 Billion </td>
</tr>
<tr>
 <th> 5 </th>
 <td> Symantic </td>
 <td> 5.6 Billion </td>
</tr>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()