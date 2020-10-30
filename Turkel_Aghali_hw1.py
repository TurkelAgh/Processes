import urllib.request   
from concurrent.futures.thread import ThreadPoolExecutor   
import time      
import os        

myCPUs = os.cpu_count()           

toDownload = dict()     
toDownload['file1'] = 'http://www.ubicomp.org/ubicomp2003/adjunct_proceedings/proceedings.pdf'         
toDownload['file2'] = 'https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf'                            
toDownload['file3'] = 'https://ars.els-cdn.com/content/image/1-s2.0-S0140673617321293-mmc1.pdf'        
toDownload['file4'] = 'http://www.visitgreece.gr/deployedFiles/StaticFiles/maps/Peloponnese_map.pdf'   



while True:
    try:
        mode = int(input('Yourapp thread mode: (thread_mode=0 -> single threaded, thread_mode=1 -> multi-threaded) :  '))
        assert mode in [0, 1]
    except Exception:                 
        print('Invalid input. Please try again...')
        continue
    else:
        break


programStart = time.time()        
if mode == 0:        
    print('Mode: Single threaded')
    for file in toDownload:
        path = file + '.pdf'
        req = urllib.request.Request(toDownload[file], headers={'User-Agent': 'Chrome'})     
        with open(path, 'wb') as f:             
            f.write(urllib.request.urlopen(req).read())       
        print(f'{file} -> done')

else:               
    print('Mode: Multi-threaded')
    def functionOnThread(fileName):      
        req = urllib.request.Request(toDownload[fileName], headers={'User-Agent': 'Chrome'})
        with open(fileName + '.pdf', 'wb') as f:
            f.write(urllib.request.urlopen(req).read())
        print(f'{file} -> done')
    with ThreadPoolExecutor(max_workers=min(4, myCPUs)) as multiThreading:       
                                                                                 
        for file in toDownload:
            multiThreading.submit(functionOnThread, file)                       


programEnd = time.time()           
print(f'Time: {round(programEnd - programStart, 2)} sec')    