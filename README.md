# StreamAutomation
The automation of assigning video permissions on MS Stream.

Can either assign owner permissions to all videos hosted by an individual or a set of specific videos - configured by a json file.

## Input File
The input json file should be named *StreamAutomation-Input.json* and should look like the one of the following. 
Keep in mind that the authorization token will be much longer than presented below.
  
  For all videos by a specified owner:
  ```
  {
    "all": true,
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbWkdldyJ9.eyJhdWQiOzaWQiOiJTLTybch1SLjw3U_QbeQ...",
    "previous_owner_id": "2785b38a10-e99d-41f5-bc7f-9d704c8ffd7b",
    "new_owner_id": "89beb98a-69a5-48b0-a938-871bd9e8017b",
    "top": 100,
    "skip": 0
  }
  ```
  
  For specific videos:
  ```
  {
  "all": false,
  "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbWkdldyJ9.eyJhdWQiOzaWQiOiJTLTybch1SLjw3U_QbeQ...",
  "new_owner_id": "89beb98a-69a5-48b0-a938-871bd9e8017b",
  "video_ids": ["8343202a-8132-4c1e-a6db-df8a117e3972", "23fa2924-eb24-4437-992f-dea3de1731f6"]
  }
  ```
  
## Getting User IDs
Do this

## Getting Authorization token
Do this

## Getting Video IDs
Do this
