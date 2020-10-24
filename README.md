## Setting up your GitHub Repository

### Installing the pre-requisities

        pip3 install -r requirements.txt

### Getting and storing 10 pages of google search result

For getting and storing the first 10 pages of google search result you firstly need to edit the **config.py** and replace the following with yours

        credentials = dict(
            my_api_key = 'YOUR API Key',
            my_cse_id = 'YOUR CSE ID',
        )

After that save your file.

Than run following command

        python3 cse.py 


and **google_search.json** file will be created in your current directory.

#### Visualize the google_search.json file

To visualize the google_search.json file install **fx**. For installing the **fx** firstly you need to install the node enter the following command to install the node.js (npm also included in it):

        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash # install nvm
        . ~/.nvm/nvm.sh # activate nvm
        nvm install node # install node.js
        node -e "console.log('Running Node.js ' + process.version)" # check if node.js is installed

Once node.js is installed. We need to install fx for this enter the following command:

        npm install -g fx

Once fx is successfully installed than issue the following command and view the google_search.json file in terminal.

    
        fx google_search.json

### Prepare youtube data for indexing

Firstly we need to enable the Youtube Data API, after enabling the youtube data API download your client secret json file and place it in the same folder. Now edit the **download_youtube_data.py** file and add the path of your client secret json file

Find this line

        CLIENT_SECRETS_FILE = "YOUR_CLIENT_SECRET_JSON_FILE"

Enter your CLIENT\_SECRET\_JSON_FILE Path and save it.

For this we need to have the youtube video\_ids.txt file which will contain the video_ids so that we can get the youtube data of corresponding video ids.

#### Get video_ids.txt file

To get the video_ids.txt file we have two options

###### Download from wget

        wget https://github.com/COSC381-2020Fall/course_project/raw/master/video_ids.txt

###### Prepare from google_search.txt file

For this download the google\_search.txt file through wget command and than prepare the video_ids.txt file

        wget https://raw.githubusercontent.com/COSC381-2020Fall/course_project/master/google_search.txt

Once the file is downloaded. Now use the following command in the terminal to create the video_ids.txt file

        grep -o 'videoid.*' google_search.txt | cut -f2- -d: | tr -d {}[], > video_ids.txt

#### Get the data_for_indexing.json file

Now execute the following command to get the \data\_for\_indexing.json file 
 
        bash download_youtube_data_batch.sh video_ids.txt

Now after executing the file we have the result stored in data_for_indexing.json file.


#### Visualize data_for_indexing.json file using fx:

        fx data_for_indexing.json

