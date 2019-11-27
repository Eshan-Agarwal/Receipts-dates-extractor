import os

# Configure google vision api key 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="config/OCR-task-8c6b6f4f9e26.json"   
from google.cloud import vision
import pandas as pd
import re


"""Detects text in the file."""

import io


a = 0
def extract_dates(path):     


           
        """Responds to any Receipts images.
        Args:
            Receipt images of any type {.png,.jpg,.jpeg etc}.
        Returns:
            Date & time if present on receipt images otherwise NULL
        """

        client = vision.ImageAnnotatorClient()   

        with io.open(path, 'rb') as image_file:
            content = image_file.read()


        image = vision.types.Image(content=content)

        # Conncets client to document_text_detection in vision api which return text from images
        response = client.document_text_detection(image=image)  # For more details about document_text_detection visit : https://cloud.google.com/vision/docs/ocr
        texts = response.full_text_annotation.text              # Extract only text as document_text_detection return text along with pixel value where it was founded

        # Below we are process extracted text through regular expressions (https://www.w3schools.com/python/python_regex.asp) to extract only dates in images.
        process_text = re.sub(', ', '\'', texts)
        process_text = re.sub(' / ', ' #', process_text)
        process_text = re.sub('/ ', '/', process_text)
        process_text = re.sub('[.] ', '\'', process_text)
        process_text = re.sub('DATE:-', ' ',process_text)
        process_text = re.sub('DATE : ', '',process_text)
        process_text = re.sub('DATE ', '',process_text)
        process_text = re.sub('DATE:-', ' ',process_text)
        process_text = re.sub('DATE: ', ' #',process_text)
        process_text = re.sub('DATE:', ' #',process_text)
        process_text = re.sub('TIME :', ' ',process_text)
        process_text = re.sub('TIME:', ' ',process_text)
        process_text = re.sub('Date:-', ' ',process_text)
        process_text = re.sub('Date : ', ' #',process_text)
        process_text = re.sub('Date :', ' #',process_text)
        process_text = re.sub('Date: ', ' #',process_text)
        process_text = re.sub('Date ', '',process_text)
        process_text = re.sub('Date:', ' #',process_text)
        process_text = re.sub('Date:-', ' ',process_text)
        process_text = re.sub('Time :', ' ',process_text)
        process_text = re.sub('Time:', ' ',process_text)
        process_text = re.sub('JANUARY ', 'Jan',process_text)
        process_text = re.sub('FEBRUARY ', 'Feb',process_text)
        process_text = re.sub('MARCH ', 'Mar',process_text)
        process_text = re.sub('APRIL ', 'Apr',process_text)
        process_text = re.sub('MAY ', 'May',process_text)
        process_text = re.sub('JUNE ', 'Jun',process_text)
        process_text = re.sub('JULY ', 'Jul',process_text)
        process_text = re.sub('AUGUST ', 'Aug',process_text)
        process_text = re.sub('SEPTEMBER ', 'Sep',process_text)
        process_text = re.sub('OCTOBER ', 'Oct',process_text)
        process_text = re.sub('NOVEMBER ', 'Nov',process_text)
        process_text = re.sub('DECEMBER ', 'Dec',process_text)
        process_text = re.sub(' Jan ', 'Jan\'',process_text)
        process_text = re.sub(' Feb ', 'Feb\'',process_text)
        process_text = re.sub(' Mar ', 'Mar\'',process_text)
        process_text = re.sub(' Apr ', 'Apr\'',process_text)
        process_text = re.sub(' May ', 'May\'',process_text)
        process_text = re.sub(' Jun ', 'Jun\'',process_text)
        process_text = re.sub(' Jul ', 'Jul\'',process_text)
        process_text = re.sub(' Aug ', 'Aug\'',process_text)
        process_text = re.sub(' Sep ', 'Sep\'',process_text)
        process_text = re.sub(' Oct ', 'Oct\'',process_text)
        process_text = re.sub(' Nov ', 'Nov\'',process_text)
        process_text = re.sub(' Dec ', 'Dec\'',process_text)

        process_text = re.sub('Jan ', 'Jan',process_text)
        process_text = re.sub('Feb ', 'Feb',process_text)
        process_text = re.sub('Mar ', 'Mar',process_text)
        process_text = re.sub('Apr ', 'Apr',process_text)
        process_text = re.sub('May ', 'May',process_text)
        process_text = re.sub('Jun ', 'Jun',process_text)
        process_text = re.sub('Jul ', 'Jul',process_text)
        process_text = re.sub('Aug ', 'Aug',process_text)
        process_text = re.sub('Sep ', 'Sep',process_text)
        process_text = re.sub('Oct ', 'Oct',process_text)
        process_text = re.sub('Nov ', 'Nov',process_text)
        process_text = re.sub('Dec ', 'Dec',process_text)


        process_text = re.sub(' JAN', 'Jan',process_text)
        process_text = re.sub(' FEB', 'Feb',process_text)
        process_text = re.sub(' MAR', 'Mar',process_text)
        process_text = re.sub(' APR', 'Apr',process_text)
        process_text = re.sub(' MAY', 'May',process_text)
        process_text = re.sub(' JUN', 'Jun',process_text)
        process_text = re.sub(' JUL', 'Jul',process_text)
        process_text = re.sub(' AUG', 'Aug',process_text)
        process_text = re.sub(' SEP', 'Sep',process_text)
        process_text = re.sub(' OCT', 'Oct',process_text)
        process_text = re.sub(' NOV', 'Nov',process_text)
        process_text = re.sub(' DEC', 'Dec',process_text)

        process_text = re.sub( '\d{6,} ', '  #',process_text)
        process_text = re.sub('\d{5,} ', ' ',process_text)
        process_text = re.sub('\d{5,}', '',process_text)
        #process_text = re.sub('\d{3} ', '  -',process_text)
        process_text = re.sub(' \d{1} ', '  #',process_text)
        process_text = re.sub(' \d{2} ', '  #',process_text)
        process_text = re.sub(': ', ' #',process_text)
        process_text = re.sub(' - ', '',process_text)
        process_text = re.sub(' PM', 'PM',process_text)
        process_text = re.sub('[a-z] ', '  #',process_text)
        process_text = re.sub(':\d{2,} ', '  #',process_text)
        process_text = re.sub('\d{3,}/\d{1,} ', ' #',process_text)
        process_text = re.sub(' \d{2}/\d{1}', '',process_text)
        process_text = re.sub('-\d{1} ', ' #',process_text)
        process_text = re.sub('\d{1,} \d{1,} \d{1,} \d{1,} \d{1,}',' #',process_text)
        process_text = re.sub('.00',' #',process_text)
        process_text = re.sub(' #', ' ',process_text)
        process_text = re.sub('today', '',process_text)
        process_text = re.sub(',', '',process_text)
        process_text = re.sub('\'[A-Z]',' #',process_text)






        # Make pandas DataFrame to store dates and time stored in process_text

        df = pd.DataFrame(columns = ['date_time'])
        for text_description in process_text.split():  # Split text description when space is encountered.


            try:
                ts = pd.to_datetime(text_description) # pd.to_datetime it stores only text_description which have dates or time in any format.
                                                      # for more info(https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
                df = df.append(            # append all dates and time.
                    dict(

                         date_time = text_description
                        ),ignore_index = True)

            except (ValueError, OverflowError):
                pass


        # Below define conditions to return only date and time as a final result because pd.to_datetime also return digits as a dates according to unix time.
        # so we create some rules and conditions for different len of dataframe.

        if (len(df.date_time) == 0):   # if df have no values that means their is no date present in image so returns NULL
                
                a = "NULL"
               



        if (len(df.date_time) == 1):
                    if not df.empty:
                        if not df.date_time[0].isdigit():
                            a = df.date_time[0]
                             

        if (len(df.date_time) == 1):
                    if not df.empty: 
                        if df.date_time[0].isdigit() :
                            a = "NULL"


        if (len(df.date_time) == 2):
                    if not df.empty:
                        if not df.date_time[0].isdigit(): 
                            if not df.date_time[1].isdigit():
                                if not (df.date_time[0] == df.date_time[1]):
                                    
                                    a = df.date_time[0] + " " + (df.date_time[1])
                                    
                                if (df.date_time[0] == df.date_time[1]):
                                    a = df.date_time[0]
                             

        if (len(df.date_time) == 2):
                    if not df.empty:                
                        if df.date_time[0].isdigit() : 
                            if not df.date_time[1].isdigit(): 
                                a = df.date_time[1]
                               

        if (len(df.date_time) == 2):
                    if not df.empty:         
                        if df.date_time[1].isdigit() : 
                            if not df.date_time[0].isdigit(): 
                                a = df.date_time[0]
                              


        if (len(df.date_time) == 2):
                    if not df.empty:         
                        if df.date_time[0].isdigit() : 
                            if df.date_time[1].isdigit() :
                                a = "NULL"
                              
                                
        
                              


        if (len(df.date_time) == 3):
                    if not df.empty:
                        if df.date_time[0].isdigit() : 
                            if df.date_time[1].isdigit() :
                                if df.date_time[2].isdigit() :
                                    a = "NULL"
                                 



        if (len(df.date_time) == 3):
                    if not df.empty:
                        if not df.date_time[0].isdigit() : 
                            if not df.date_time[1].isdigit() :
                                if not df.date_time[2].isdigit() :
                                    if not (df.date_time[0] == df.date_time[1] == df.date_time[2]):
                                        a = df.date_time[0] + " " + (df.date_time[1]) + " " + (df.date_time[2])
                                    
                                    if (df.date_time[0] == df.date_time[1] != df.date_time[2]): 
                                        a = df.date_time[0] + " " + (df.date_time[2])
                                        
                                    if (df.date_time[0] == df.date_time[2] != df.date_time[1]): 
                                        a = df.date_time[0] + " " + (df.date_time[1])
                                        
                                    if (df.date_time[1] == df.date_time[2] != df.date_time[0]): 
                                        a = df.date_time[0] + " " + (df.date_time[1])
                                    
                                    if (df.date_time[0] == df.date_time[1] == df.date_time[2]):
                                        a = df.date_time[0]
                                    


        if (len(df.date_time) == 3):
                    if not df.empty:
                        if df.date_time[0].isdigit():
                            if df.date_time[1].isdigit():
                                if not df.date_time[2].isdigit():
                                    a = df.date_time[2]
                              



        if (len(df.date_time) == 3):
                    if not df.empty:
                        if df.date_time[0].isdigit():
                            if df.date_time[2].isdigit():
                                if not df.date_time[1].isdigit():
                                    a = df.date_time[1]
                                  


        if (len(df.date_time) == 3):
                        if not df.empty:
                            if df.date_time[1].isdigit():
                                if df.date_time[2].isdigit():
                                    if not df.date_time[0].isdigit():
                                            a = df.date_time[0]
                                         


        if (len(df.date_time) == 3):
                        if not df.empty:
                            if df.date_time[0].isdigit():
                                if not df.date_time[1].isdigit():
                                    if not df.date_time[2].isdigit():
                                        if not (df.date_time[1] == df.date_time[2]):
                                            a = df.date_time[1] + " " + (df.date_time[2])
                                            
                                        if (df.date_time[1] == df.date_time[2]):
                                            a = df.date_time[1]
                                   


        if (len(df.date_time) == 3):
                        if not df.empty:
                            if df.date_time[1].isdigit():
                                if not df.date_time[0].isdigit():
                                    if not df.date_time[2].isdigit():
                                        if not (df.date_time[0] == df.date_time[2]):
                                            a = df.date_time[0] + " " + (df.date_time[2])
                                            
                                        if (df.date_time[0] == df.date_time[2]):
                                            a = df.date_time[0]
                                    



        if (len(df.date_time) == 3):
                        if not df.empty:
                            if df.date_time[2].isdigit():
                                if not df.date_time[0].isdigit():
                                    if not df.date_time[1].isdigit():
                                        if not (df.date_time[0] == df.date_time[1]):
                                            a = df.date_time[0] + " " + (df.date_time[1])
                                            
                                        if (df.date_time[0] == df.date_time[1]):
                                             a = df.date_time[0]
                                                


        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[0].isdigit(): 
                                 if df.date_time[1].isdigit():
                                    if df.date_time[2].isdigit():
                                        if df.date_time[2].isdigit():
                                            a = "NULL"
                                              

        if (len(df.date_time) == 4):
                if not df.empty:
                    if not df.date_time[0].isdigit(): 
                         if not df.date_time[1].isdigit():
                            if not df.date_time[2].isdigit():
                                if not df.date_time[3].isdigit():
                                    if not (df.date_time[0] == df.date_time[1] == df.date_time[2]== df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[1]) + " " + (df.date_time[2]) + " " + (df.date_time[3])
                                            
                                    if (df.date_time[0] == df.date_time[1] == df.date_time[2]== df.date_time[3]):
                                            a = df.date_time[0]
                                    
                                    if (df.date_time[0] == df.date_time[1] == df.date_time[2]!= df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[3])
                                            
                                    if (df.date_time[0] == df.date_time[1] == df.date_time[3]!= df.date_time[2]):
                                            a = df.date_time[0] + " " + (df.date_time[2])
                                            
                                    if (df.date_time[1] == df.date_time[2] == df.date_time[3]!= df.date_time[0]):
                                            a = df.date_time[0] + " " + (df.date_time[1])
                                            
                                    if (df.date_time[0] == df.date_time[2] == df.date_time[3]!= df.date_time[1]):
                                            a = df.date_time[0] + " " + (df.date_time[1])
                                            
                                            
                                    if (df.date_time[0] == df.date_time[1] != df.date_time[2]== df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[2])
                                            
                                    if (df.date_time[0] == df.date_time[2] != df.date_time[1]== df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[1])
                                            
                                    if (df.date_time[0] == df.date_time[3] != df.date_time[1]== df.date_time[2]):
                                            a = df.date_time[0] + " " + (df.date_time[2])
                                            
                                    if (df.date_time[1] == df.date_time[2] != df.date_time[0]== df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[1])
                                            
                                    if (df.date_time[2] == df.date_time[3] != df.date_time[1]== df.date_time[0]):
                                            a = df.date_time[0] + " " + (df.date_time[2])
                                            
                                            
                                    
                                    if (df.date_time[0] == df.date_time[1] != df.date_time[2]!= df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[2]) + " " + (df.date_time[3])
                                            
                                    if (df.date_time[0] == df.date_time[2] != df.date_time[1]!= df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[1])+ " " + (df.date_time[3])
                                            
                                    if (df.date_time[0] == df.date_time[3] != df.date_time[1]!= df.date_time[2]):
                                            a = df.date_time[0] + " " + (df.date_time[1])+ " " + (df.date_time[2])
                                            
                                    if (df.date_time[1] == df.date_time[2] != df.date_time[0]!= df.date_time[3]):
                                            a = df.date_time[0] + " " + (df.date_time[1])+ " " + (df.date_time[3])
                                            
                                    if (df.date_time[2] == df.date_time[3] != df.date_time[1]!= df.date_time[0]):
                                            a = df.date_time[0] + " " + (df.date_time[1])+ " " + (df.date_time[2])        
                                            
                                    
                                            
                                    

        if (len(df.date_time) == 4):
                if not df.empty:
                    if df.date_time[0].isdigit(): 
                         if not df.date_time[1].isdigit():
                            if not df.date_time[2].isdigit():
                                if not df.date_time[3].isdigit():
                                    
                                        if not (df.date_time[1] == df.date_time[2] == df.date_time[3]):
                                            a = (df.date_time[1]) + " " + (df.date_time[2]) + " " + (df.date_time[3])

                                        if (df.date_time[1] == df.date_time[2] != df.date_time[3]): 
                                            a = df.date_time[1] + " " + (df.date_time[3])

                                        if (df.date_time[1] == df.date_time[3] != df.date_time[2]): 
                                            a = df.date_time[1] + " " + (df.date_time[2])

                                        if (df.date_time[2] == df.date_time[3] != df.date_time[1]): 
                                            a = df.date_time[1] + " " + (df.date_time[2])

                                
                                                                         
                                    
                                    
                                    
        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[1].isdigit(): 
                                 if not df.date_time[0].isdigit():
                                    if not df.date_time[2].isdigit():
                                        if not df.date_time[3].isdigit():
                                                                         
                                            if not (df.date_time[0] == df.date_time[2] == df.date_time[3]):
                                                a = (df.date_time[0]) + " " + (df.date_time[2]) + " " + (df.date_time[3])

                                            if (df.date_time[0] == df.date_time[2] != df.date_time[3]): 
                                                a = df.date_time[0] + " " + (df.date_time[3])

                                            if (df.date_time[0] == df.date_time[3] != df.date_time[2]): 
                                                a = df.date_time[0] + " " + (df.date_time[2])

                                            if (df.date_time[2] == df.date_time[3] != df.date_time[0]): 
                                                a = df.date_time[0] + " " + (df.date_time[2])
                                                    

                                            
        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[2].isdigit(): 
                                 if not df.date_time[0].isdigit():
                                    if not df.date_time[1].isdigit():
                                        if not df.date_time[3].isdigit():
                                                                         
                                                                         
                                            if not (df.date_time[0] == df.date_time[1] == df.date_time[3]):
                                                a = (df.date_time[0]) + " " + (df.date_time[1]) + " " + (df.date_time[3])

                                            if (df.date_time[0] == df.date_time[1] != df.date_time[3]): 
                                                a = df.date_time[0] + " " + (df.date_time[3])

                                            if (df.date_time[0] == df.date_time[3] != df.date_time[1]): 
                                                a = df.date_time[0] + " " + (df.date_time[1])

                                            if (df.date_time[1] == df.date_time[3] != df.date_time[0]): 
                                                a = df.date_time[0] + " " + (df.date_time[1])
                                            
                                            
                                            
        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[3].isdigit(): 
                                 if not df.date_time[0].isdigit():
                                    if not df.date_time[1].isdigit():
                                        if not df.date_time[2].isdigit():
                                                                    
                                            if not (df.date_time[0] == df.date_time[1] == df.date_time[2]):
                                                a = (df.date_time[0]) + " " + (df.date_time[1]) + " " + (df.date_time[2])

                                            if (df.date_time[0] == df.date_time[1] != df.date_time[2]): 
                                                a = df.date_time[0] + " " + (df.date_time[2])

                                            if (df.date_time[0] == df.date_time[2] != df.date_time[1]): 
                                                a = df.date_time[0] + " " + (df.date_time[1])

                                            if (df.date_time[1] == df.date_time[2] != df.date_time[0]): 
                                                a = df.date_time[0] + " " + (df.date_time[1])
                                            

        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[0].isdigit():
                                if df.date_time[1].isdigit():
                                    if not df.date_time[2].isdigit():
                                        if not df.date_time[3].isdigit():
                                                                         
                                                if not (df.date_time[2] == df.date_time[3]):
                                                    a = df.date_time[2] + " " + (df.date_time[3])
                                                                         
                                                if (df.date_time[2] == df.date_time[3]):
                                                                         
                                                    a = df.date_time[2]
                                            

        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[0].isdigit():
                                if df.date_time[2].isdigit():
                                    if not df.date_time[1].isdigit():
                                        if not df.date_time[3].isdigit():
                                                                         
                                            if not (df.date_time[1] == df.date_time[3]):
                                                    a = df.date_time[1] + " " + (df.date_time[3])
                                                                         
                                            if (df.date_time[1] == df.date_time[3]):
                                                                         
                                                    a = df.date_time[1]
                                            
                                          

        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[0].isdigit():
                                if df.date_time[3].isdigit():
                                    if not df.date_time[1].isdigit():
                                        if not df.date_time[2].isdigit():
                                                                         
                                            if not (df.date_time[1] == df.date_time[2]):
                                                    a = df.date_time[1] + " " + (df.date_time[2])
                                                                         
                                            if (df.date_time[1] == df.date_time[2]):
                                                                         
                                                    a = df.date_time[2]
                                            
                                         

        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[1].isdigit():
                                if df.date_time[2].isdigit():
                                    if not df.date_time[0].isdigit():
                                        if not df.date_time[3].isdigit():
                                                                         
                                            if not (df.date_time[0] == df.date_time[3]):
                                                    a = df.date_time[0] + " " + (df.date_time[3])
                                                                         
                                            if (df.date_time[0] == df.date_time[3]):
                                                                         
                                                    a = df.date_time[0]
                                            
                                         

        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[1].isdigit():
                                if df.date_time[3].isdigit():
                                    if not df.date_time[0].isdigit():
                                        if not df.date_time[2].isdigit():
                                                                         
                                            if not (df.date_time[0] == df.date_time[2]):
                                                     a = df.date_time[0] + " " + (df.date_time[2])
                                                                         
                                            if (df.date_time[0] == df.date_time[2]):
                                                                         
                                                    a = df.date_time[0]
                                           
                                        

        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[2].isdigit():
                                if df.date_time[3].isdigit():
                                    if not df.date_time[0].isdigit():
                                        if not df.date_time[1].isdigit():
                                                                         
                                            if not (df.date_time[0] == df.date_time[1]):
                                                     a = df.date_time[0] + " " + (df.date_time[1])
                                                                         
                                            if (df.date_time[0] == df.date_time[1]):
                                                                         
                                                    a = df.date_time[0]
                                            
                                        


        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[0].isdigit():
                                if df.date_time[1].isdigit():
                                    if df.date_time[2].isdigit():
                                        if not df.date_time[3].isdigit():
                                            a = df.date_time[3] 
                                         


        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[0].isdigit():
                                if df.date_time[1].isdigit():
                                    if df.date_time[3].isdigit():
                                        if not df.date_time[2].isdigit():
                                            a = df.date_time[2] 
                                         


        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[1].isdigit():
                                if df.date_time[2].isdigit():
                                    if df.date_time[3].isdigit():
                                        if not df.date_time[0].isdigit():
                                            a = df.date_time[0] 
                                           



        if (len(df.date_time) == 4):
                        if not df.empty:
                            if df.date_time[0].isdigit():
                                if df.date_time[2].isdigit():
                                    if df.date_time[3].isdigit():
                                        if not df.date_time[1].isdigit():
                                            a = df.date_time[1] 
                                                                         
                                                                         
        
        if (len(df.date_time) >= 4):
                        if not df.empty:
                    
                            if not df.date_time[0].isdigit():
                                    
                                  a = df.date_time[0]                                       
                                                                         




    
        return a







