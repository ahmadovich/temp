import re
import random
import argparse
import os

def modifytime(infile,mydelta):
    ignored_lines = 0
    #This will compile a pattern for 5 different regex groups.
    pattern = re.compile(r'(\d\d:\d\d:\d\d,\d\d\d)(\s*)(-->)(\s*)(\d\d:\d\d:\d\d,\d\d\d)')
    
    with open(os.path.split(args.subfile)[0]+'\\fixed.srt','w') as outfile:
       
        for lines in infile:
                match = re.search(pattern,lines)
                if match:
                    starttime = (match.group(1)).split(':') #Time start
                    endtime = (match.group(5)).split(':') #Time end
                    start_seconds_split = starttime[2].split(',')
                    start_seconds = int(start_seconds_split[0]) + (int(start_seconds_split[1]) / 1000)
                    start_total_seconds = ((int(starttime[0]) *3600) + (int(starttime[1]) *60) + int(start_seconds)) + mydelta
                    end_seconds_split = endtime[2].split(',')
                    end_seconds = int(end_seconds_split[0]) + (int(end_seconds_split[1]) / 1000)
                    print(start_seconds,end_seconds)
                    end_total_seconds = ((int(endtime[0]) *3600) + (int(endtime[1]) *60) + int(end_seconds)) + mydelta
                    #check if new value is less than 0 ( not allowed ), we can only check on start time only if we want.
                    if start_total_seconds < 0  or end_total_seconds < 0:
                        ignored_lines += 1
                        #if new time is < 0 then keep the original timing for start and end
                        new_start_formatted = match.group(1)
                        new_end_formatted = match.group(5)
                        if ignored_lines > 2 :
                            print('Exiting, too many lines were ignored')
                            exit(2)
                        else:
                            newlineformatted = new_start_formatted +' '+'-->'+' '+new_end_formatted
                            outfile.write(str(newlineformatted) + '\n')
                    else:
                        # Here we calculate new time and put it in the correct string format
                        new_start_formatted = formattime(start_total_seconds)
                        new_end_formatted = formattime(end_total_seconds)
                        newlineformatted = new_start_formatted +' '+'-->'+' '+new_end_formatted
                        outfile.write(str(newlineformatted ) + '\n')
                            
                                                                           
                else:
                    outfile.write(lines)
                    # here we should write other lines, like subtitles itself unchanged to the new file
                    
def formattime(time): 
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = int(time)
    milliseconds = int((time - seconds) * 1000)
    return (str(hour).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2)+','+str(milliseconds).zfill(3))
    
def main(file,delta_seconds):    
   
    with open(file,'r') as infile:
        if  abs(delta_seconds) < 600 :
            modifytime(infile, delta_seconds)
        else:
            print('Allowed change should be no more than 10 minutes')
            exit(1)
            
# start by getting parameters
parser = argparse.ArgumentParser('subtime')
parser.add_argument('-f', '--subfile', required = True, type = str, metavar = '', help = 'Path to subtitle file')
parser.add_argument('-s', '--secondsdelta', type = float, default = -3, metavar = '', help = 'Time adjustment in seconds')            
args = parser.parse_args()
print(args.subfile,args.secondsdelta)

if __name__ == '__main__': main(args.subfile,args.secondsdelta)        


''' Create timelist for each line of timings, which is a list with two members
then split each member of the list into 3 (or 4) integers
add or delete the desired change

convert everything into seconds
allow only a maximum of +- 10 minutes of adjustment
check if the value is a negative timing and ignore it for the first 3 subtitles only
'''