# Stream Automation
The automation of assigning video permissions on MS Stream.

Can either assign owner permissions to all videos hosted by an individual, viewable by a group, or a set of specific videos - configured by a json file.

## Input File
The input json file should be named ***StreamAutomation-Input.json*** and should look like the one of the following. 
Keep in mind that the authorization token will be much longer than presented below and top is capped at 100.
Details on how to find IDs are detailed further down.
  
  ### For all videos uploaded by a specific user:
  ```
  {
    "processing": "user",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbWkdldyJ9.eyJhdWQiOzaWQiOiJTLTybch1SLjw3U_QbeQ...",
    "previous_owner_id": "2785b38a10-e99d-41f5-bc7f-9d704c8ffd7b",
    "new_owner_id": "89beb98a-69a5-48b0-a938-871bd9e8017b",
    "top": 100,
    "skip": 0
  }
  ```
  ### For all videos viewable by a specific group:
  ```
  {
    "processing": "group",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbWkdldyJ9.eyJhdWQiOzaWQiOiJTLTybch1SLjw3U_QbeQ...",
    "group_id": "6cd7779f-cea8-4a3c-8e87-19a16afcf919",
    "new_owner_id": "89beb98a-69a5-48b0-a938-871bd9e8017b",
    "top": 100,
    "skip": 0
  }
  ```
  
### For specific videos:

```
{
  "processing": "videos",
  "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbWkdldyJ9.eyJhdWQiOzaWQiOiJTLTybch1SLjw3U_QbeQ...",
  "new_owner_id": "89beb98a-69a5-48b0-a938-871bd9e8017b",
  "video_ids": ["8343202a-8132-4c1e-a6db-df8a117e3972", "23fa2924-eb24-4437-992f-dea3de1731f6"]
}
```
  
## Getting input details
This section will explain how to find the appropriate details to put in the json input file.
### Video IDs
On Stream, the video ID is contained in the URL. For example the ID for this video:

`https://web.microsoftstream.com/video/fba2ada4-3e0e-47f4-9896-3249c2566785`

is `fba2ada4-3e0e-47f4-9896-3249c2566785`

### User and Group IDs
User and group IDs can be found in a similar way as stated above, however you can also find
the IDs on AAD. 
Search the user/group in question and find their "Object Id".

To confirm this is the right ID go to the following links swapping out "ID" for the object ID.
This should bring you to the group/user's Stream page.

`https://web.microsoftstream.com/group/ID`

`https://web.microsoftstream.com/user/ID`

### Top and Skip
`Top` and `skip` refer to how many videos to process, they should be entered as **positive integers** 
(not strings i.e. no quotes)

`Top` is capped at 100 by the webserver, any number entered that's greater than 100 will be set to 100.
Due to this limitation, skip is used to *skip* over the first `skip` amount of videos. 
**To process more than 100 videos**, the program will need to be rerun, where `skip` is increased by 100 each time.

### Authorization
Unfortunately getting the authorization token does take a little more work.

- Go to stream in admin mode;
- Open up 'inspect element' / 'developer tools' - right click and select 'inspect';
- In the developer tools window, select 'Network' tab at the top;
- Filter by "Fetch/XHR";
- Click any link on Stream, the network tab should fill up requests;
- Find one that contains a question mark e.g. "events?...", "videos?...";
- Look through the request headers to find the authorization token;
- Copy the entire string **including 'Bearer'**.
