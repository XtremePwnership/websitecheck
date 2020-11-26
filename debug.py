
2020-11-26T11:32:20.483567+00:00 heroku[scheduler.6258]: Starting process with command `python myPythonFile.py`                
2020-11-26T11:32:21.201660+00:00 heroku[scheduler.6258]: State changed from starting to up                              
2020-11-26T11:32:24.772421+00:00 app[scheduler.6258]: entered checker                                                   
2020-11-26T11:34:32.583421+00:00 app[scheduler.6258]: Traceback (most recent call last):                                
2020-11-26T11:34:32.583462+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/connection.py", line 160, in _new_conn                                                                                      
2020-11-26T11:34:32.583854+00:00 app[scheduler.6258]: (self._dns_host, self.port), self.timeout, **extra_kw             
2020-11-26T11:34:32.583859+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/util/connection.py", line 84, in create_connection                                                                          
2020-11-26T11:34:32.584054+00:00 app[scheduler.6258]: raise err                                                         
2020-11-26T11:34:32.584060+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/util/connection.py", line 74, in create_connection                                                                          
2020-11-26T11:34:32.584259+00:00 app[scheduler.6258]: sock.connect(sa)                                                  
2020-11-26T11:34:32.584266+00:00 app[scheduler.6258]: TimeoutError: [Errno 110] Connection timed out                    
2020-11-26T11:34:32.584293+00:00 app[scheduler.6258]:                                                                   
2020-11-26T11:34:32.584295+00:00 app[scheduler.6258]: During handling of the above exception, another exception occurred:                                                                                                                       
2020-11-26T11:34:32.584295+00:00 app[scheduler.6258]:                                                                   
2020-11-26T11:34:32.584300+00:00 app[scheduler.6258]: Traceback (most recent call last):                                
2020-11-26T11:34:32.584304+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/connectionpool.py", line 677, in urlopen                                                                                    
2020-11-26T11:34:32.584834+00:00 app[scheduler.6258]: chunked=chunked,                                                  
2020-11-26T11:34:32.584839+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/connectionpool.py", line 381, in _make_request                                                                              
2020-11-26T11:34:32.585229+00:00 app[scheduler.6258]: self._validate_conn(conn)                                         
2020-11-26T11:34:32.585234+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/connectionpool.py", line 978, in _validate_conn                                                                             
2020-11-26T11:34:32.595791+00:00 app[scheduler.6258]: conn.connect()                                                    
2020-11-26T11:34:32.595803+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/connection.py", line 309, in connect                                                                                        
2020-11-26T11:34:32.596337+00:00 app[scheduler.6258]: conn = self._new_conn()                                           
2020-11-26T11:34:32.596342+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/connection.py", line 172, in _new_conn                                                                                      
2020-11-26T11:34:32.596633+00:00 app[scheduler.6258]: self, "Failed to establish a new connection: %s" % e              
2020-11-26T11:34:32.596679+00:00 app[scheduler.6258]: urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPSConnection object at 0x7feff67a5518>: Failed to establish a new connection: [Errno 110] Connection timed out              
2020-11-26T11:34:32.596769+00:00 app[scheduler.6258]:                                                                   
2020-11-26T11:34:32.596770+00:00 app[scheduler.6258]: During handling of the above exception, another exception occurred:                                                                                                                       
2020-11-26T11:34:32.596770+00:00 app[scheduler.6258]:                                                                   
2020-11-26T11:34:32.596806+00:00 app[scheduler.6258]: Traceback (most recent call last):                                
2020-11-26T11:34:32.596812+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/requests/adapters.py", line 449, in send                                                                                            
2020-11-26T11:34:32.597411+00:00 app[scheduler.6258]: timeout=timeout                                                   
2020-11-26T11:34:32.597417+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/connectionpool.py", line 727, in urlopen                                                                                    
2020-11-26T11:34:32.598366+00:00 app[scheduler.6258]: method, url, error=e, _pool=self, _stacktrace=sys.exc_info()[2]   
2020-11-26T11:34:32.598367+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/urllib3/util/retry.py", line 446, in increment                                                                                      
2020-11-26T11:34:32.598880+00:00 app[scheduler.6258]: raise MaxRetryError(_pool, url, error or ResponseError(cause))    
2020-11-26T11:34:32.598898+00:00 app[scheduler.6258]: urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.xyz.com', port=443): Max retries exceeded with url: xxx (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7feff67a5518>: Failed to establish a new connection: [Errno 110] Connection timed out',))                            
2020-11-26T11:34:32.598902+00:00 app[scheduler.6258]:                                                                   
2020-11-26T11:34:32.598903+00:00 app[scheduler.6258]: During handling of the above exception, another exception occurred:                                                                                                                       
2020-11-26T11:34:32.598903+00:00 app[scheduler.6258]:                                                                   
2020-11-26T11:34:32.598907+00:00 app[scheduler.6258]: Traceback (most recent call last):                                
2020-11-26T11:34:32.598941+00:00 app[scheduler.6258]: File "myPythonFile.py", line 41, in <module>                             
2020-11-26T11:34:32.599164+00:00 app[scheduler.6258]: checkIt(name, URL)                                                
2020-11-26T11:34:32.599170+00:00 app[scheduler.6258]: File "myPythonFile.py", line 26, in checkIt                              
2020-11-26T11:34:32.599375+00:00 app[scheduler.6258]: res = requests.get(myPythonFileUrl, headers=headers, verify = False)     
2020-11-26T11:34:32.599488+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/requests/api.py", line 76, in get                                                                                                   
2020-11-26T11:34:32.599754+00:00 app[scheduler.6258]: return request('get', url, params=params, **kwargs)               
2020-11-26T11:34:32.599755+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/requests/api.py", line 61, in request                                                                                               
2020-11-26T11:34:32.600338+00:00 app[scheduler.6258]: return session.request(method=method, url=url, **kwargs)          
2020-11-26T11:34:32.600343+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/requests/sessions.py", line 530, in request                                                                                         
2020-11-26T11:34:32.600983+00:00 app[scheduler.6258]: resp = self.send(prep, **send_kwargs)                             
2020-11-26T11:34:32.600985+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/requests/sessions.py", line 643, in send                                                                                            
2020-11-26T11:34:32.601550+00:00 app[scheduler.6258]: r = adapter.send(request, **kwargs)                               
2020-11-26T11:34:32.601556+00:00 app[scheduler.6258]: File "/app/.heroku/python/lib/python3.6/site-packages/requests/adapters.py", line 516, in send                                                                                            
2020-11-26T11:34:32.602014+00:00 app[scheduler.6258]: raise ConnectionError(e, request=request)                         
2020-11-26T11:34:32.602020+00:00 app[scheduler.6258]: requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.xyz.com', port=443): Max retries exceeded with url: xxx (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7feff67a5518>: Failed to establish a new connection: [Errno 110] Connection timed out',))                         
2020-11-26T11:34:32.727678+00:00 heroku[scheduler.6258]: Process exited with status 1                                   
2020-11-26T11:34:32.779259+00:00 heroku[scheduler.6258]: State changed from up to complete                                                                                                                                                                                                                                  