import json
import requests
from typing import List
import logging
from tqdm import tqdm
import traceback


def get_video_ids_from_creator(creator_id: str, top: int, skip: int, auth: str) -> List[str]:
    """Get a list of IDs for videos created by a given user

    :param creator_id: Given user id
    :param top: How many IDs?
    :param skip: How many should the program skip over?
    :param auth: Authorization token string
    :return: A list of the IDs
    """
    get_videos_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en",
        "authorization": auth,
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-ms-client-request-id": "d703f3d3-8dff-280d-ee4d-4bfc8b46d8a4",
        "x-ms-client-session-id": "b3684058-d864-4bc6-a60f-f31ae18bbb16",
        "x-ms-correlation-request-id": "dddddddd-b087-973a-490d-29ca1aa74475",
        "Referer": "https://web.microsoftstream.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    # get_videos_url = f"https://euno-1.api.microsoftstream.com/api/videos?$top={top}&$skip={skip}&$expand=creator,events&$filter=published%20and%20(state%20eq%20%27Completed%27%20or%20contentSource%20eq%20%27livestream%27)%20and%20creator%2Fid%20eq%20%{creator_id}%27&adminmode=true&api-version=1.4-private"
    get_videos_url = f"https://euno-1.api.microsoftstream.com/api/videos?$top={top}&$skip={skip}&$orderby=metrics%2FtrendingScore%20desc&$expand=events&$filter=creator%2Fid%20eq%20%27{creator_id}%27%20and%20published%20and%20(state%20eq%20%27Completed%27%20or%20contentSource%20eq%20%27livestream%27)&adminmode=true&api-version=1.4-private"
    payload = f"$top={top}&$skip={skip}&$expand=creator,events&$filter=published%20and%20(state%20eq%20%27Completed%27%20or%20contentSource%20eq%20%27livestream%27)%20and%20creator%2Fid%20eq%20%{creator_id}%27&adminmode=true&api-version=1.4-private"

    response = requests.get(get_videos_url, headers=get_videos_headers, data=payload)
    print(f"{get_videos_url=}\n\n{payload=}\n\n{response.json()=}")
    json_ = response.json()["value"]

    ids = [item['id'] for item in json_]
    # for item in json_:
    #    print(item['id'])

    return ids


def get_video_ids_from_group(group_id: str, top: int, skip: int, auth: str) -> List[str]:
    url = f"https://euno-1.api.microsoftstream.com/api/groups/{group_id}/videos?$top={top}&$skip={skip}&$orderby=metrics%2FtrendingScore%20desc&$filter=published%20and%20(state%20eq%20%27Completed%27%20or%20contentSource%20eq%20%27livestream%27)&adminmode=true&api-version=1.4-private"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en",
        "authorization": auth,
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-ms-client-request-id": "191fbd57-7d35-7dce-2a63-ed7306607a92",
        "x-ms-client-session-id": "8c68d6a1-6d24-4294-bfea-324e8c3ca4e2",
        "x-ms-correlation-request-id": "undefined-9466-e8ca-993d-2efa02c0f285",
        "Referer": "https://web.microsoftstream.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    payload = f"$top={top}&$skip={skip}&$orderby=metrics%2FtrendingScore%20desc&$filter=published%20and%20(state%20eq%20%27Completed%27%20or%20contentSource%20eq%20%27livestream%27)&adminmode=true&api-version=1.4-private"
    response = requests.get(url, headers=headers, data=payload)

    json_ = response.json()["value"]
    ids = [item["id"] for item in json_]

    return ids


def get_current_config(vid_id: str, auth: str):
    get_links_headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en",
        "authorization": auth,
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-ms-client-request-id": "e9d101a9-d215-5a0b-4df7-2bbb34c7b0fa",
        "x-ms-client-session-id": "5ea458f4-01cf-4379-bb34-b52e76475c44",
        "x-ms-correlation-request-id": "ffffffff-65af-f40f-5df2-f375dfd6eab9",
        "Referer": "https://web.microsoftstream.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    get_links_request_url = "https://euno-1.api.microsoftstream.com/api/videos/" \
                            + vid_id \
                            + "/getLinks?adminmode=true&api-version=1.4-private"
    response = requests.get(get_links_request_url, headers=get_links_headers).json()

    return response


def update_config(vid_id, payload, auth):
    set_links_headers = {
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en",
        "authorization": auth,
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-ms-client-request-id": "04e70099-b8fd-7762-c3cb-612c82793a1a",
        "x-ms-client-session-id": "5ea458f4-01cf-4379-bb34-b52e76475c44",
        "x-ms-correlation-request-id": "cccccccc-b974-1944-3229-3159ae21b227",
        "Referer": "https://web.microsoftstream.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    url = f"https://euno-1.api.microsoftstream.com/api/videos/{vid_id}/setLinks?adminmode=true&api-version=1.4-private"
    response = requests.post(url, headers=set_links_headers, data=payload)
    return response


def create_payload_for_perms(json_dict: dict, user_id: str):
    """Creates a JSON payload that will grant owner permissions

    :param json_dict: JSON like dict that contains the payload from the get request
    :param user_id: ID for the user to be given permissions
    :return: json payload
    """
    # roleAssignments = original['roleAssignments'][0]
    json_dict['roleAssignments'].append({
        "roleId": "5199031d-b5da-4bd7-acf5-2eb7db39e8f4",
        "principals": [
            {
                "principalId": f"{user_id}",
                "principalType": "User"}
        ]})
    return json.dumps(json_dict)


def run(video_ids, new_owner: str, auth: str):
    logger.info("Running Main\n")

    print(f"Video IDs selected: {video_ids}")
    logger.info(f"Video IDs selected: {video_ids}")

    # tqdm creates a progress bar
    for video_ID in tqdm(video_ids):
        logger.info(f"Video ID = {video_ID}")
        try:
            # Get links / current configuration of video
            current_config = get_current_config(vid_id=video_ID, auth=auth)
            logger.info(f"Current config: {current_config}")

            # Create a payload to add new owner
            payload = create_payload_for_perms(current_config, new_owner)
            logger.info(f"Payload: {payload}")

            # Send payload to Stream
            response = update_config(vid_id=video_ID, payload=payload, auth=auth)

            # Check response
            if response.status_code == 400 and response.content.decode() == '{"error":{"code":"BadRequest","message":"A principal can only be assigned to one role for a given resource"}}':
                logger.warning(f"Response: [{response.status_code}] - User already has permissions\n")
            elif response.status_code != 200:
                logger.error(f"Response: [{response.status_code}] - {response.content.decode()}\n")
            else:
                logger.info(f"Response: [{response.status_code}] {response.content.decode()}\n")
        except Exception as e:
            logger.error(f"ERROR - {e}")


def main():
    try:
        # Get input values from json file
        with open("StreamAutomation-Input.json", 'r') as file:
            input_values: dict = json.load(file)

        processing_type: str = input_values["processing"]
        authorization: str = input_values["authorization"]
        new_owner_id: str = input_values["new_owner_id"]

        # If the videos are processed based on who created them or a group that can view them
        # Both use top and skip
        if processing_type in "user" or "group":
            # Use int() here to confirm the values are ints - if they're not then ValueError is raised which is caught
            top: int = int(input_values["top"])
            skip: int = int(input_values["skip"])

            # top is capped at 100 by the webserver
            if top > 100:
                top = 100
            # top can't be less than 1
            elif top < 0:
                top = 1

            # can't skip a negative amount
            if skip < 0:
                skip = 0

            if processing_type == "user":
                owner_id: str = input_values["previous_owner_id"]
                video_ids: List[str] = get_video_ids_from_creator(creator_id=owner_id,
                                                                  top=top,
                                                                  skip=skip,
                                                                  auth=authorization)
            else:
                group_id: str = input_values["group_id"]
                video_ids: List[str] = get_video_ids_from_group(group_id=group_id,
                                                                top=top,
                                                                skip=skip,
                                                                auth=authorization)
        elif processing_type == "videos":
            video_ids: List[str] = input_values["video_ids"]
        else:
            logging.error(f'ERROR - Invalid processing type "{processing_type}" - should be "user", "group" or "videos"')
            print(f'ERROR - Invalid processing type "{processing_type}" - should be "user", "group" or "videos"')
            return

    except FileNotFoundError as e:
        print(f"ERROR - {e} - Input file ('StreamAutomation-Input.json') not found")
        logger.error(f"{e} - Input file ('StreamAutomation-Input.json') not found")
        return
    except KeyError as e:
        print(f"ERROR - {e} - Input file is formatted incorrectly")
        logger.error(f"{e} - Input file is formatted incorrectly")
        traceback.print_exc()
        return
    except ValueError as e:
        print(f"ERROR - {e} - Input file is formatted incorrectly")
        logger.error(f"{e} - Input file is formatted incorrectly")
        traceback.print_exc()
        return

    try:
        run(auth=authorization, new_owner=new_owner_id, video_ids=video_ids)
    except requests.exceptions.JSONDecodeError as e:
        print(f"ERROR - {e} - this usually indicates that the authorization token is incorrect / outdated")
        logger.error(f"{e} - authorization token is likely incorrect / outdated")


def get_id_from_url(url: str) -> str:
    start = url.rfind('/') + 1
    end = url.rfind('?')
    # If '?' is not in the url
    if end == -1:
        return url[start:]
    else:
        return url[start:end]


if __name__ == '__main__':
    logging.basicConfig(filename="StreamAutomation-Output.log",
                        format='%(name)s :: %(levelname)s :: %(asctime)s :: %(message)s',
                        filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # current_config = get_current_config(vid_id='d35fe72c-f7c3-47ba-abe0-e23dfef4864d')
    # payload = create_payload(current_config, '89beb98a-69a5-48b0-a938-871bd9e8017b')
    # response = update_config('d35fe72c-f7c3-47ba-abe0-e23dfef4864d', payload)

    input("Press enter to start. INPUT FILE: 'StreamAutomation-Input.json'")

    main()
