## ANSWERS

#### Questions

1. How much disk space is used after step 4?  

**After x hours running the disk space used was y.**   

2. Did you parallelize the crawlers in step 4? If so, how?  
**I started multiple crawlers, each with a subset of the 10M 188 files with deduplicated web pages (see below). The crawler.py was changed to receive the name of the file as paramenter. Then I used regex to create multiple commands in my local computer and executed them all. Example:**  

    ```
    python3 ~/lazynlp/lazynlp/crawler.py split_reg_aa & 
    ```

3. Describe the steps to de-duplicate the web pages you crawled.  
**I ran scripts that first combined and then deduplicated entries.**  
    ```
    cat RS* > ./mergedfile.txt
    sort mergedfile.txt | uniq -u > deduplicated.txt  
    sort mergedfile.txt | uniq -u > deduplicated.txt 

    ls -l --block-size=M deduplicated.txt mergedfile.txt
    -rw-r--r--. 1 root root 1868M Apr  1 12:45 deduplicated.txt
    -rw-r--r--. 1 root root 1873M Apr  1 12:38 mergedfile.txt
    
    split -b 10M deduplicated.txt split_reg_
    
    ls | wc -l
    188
    ```

4. Submit the list of files you that your LazyNLP spiders crawled (ls -la)  
**[Ouput](output.txt) of ls -la.**  