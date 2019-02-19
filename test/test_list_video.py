import onfido
import os

onfido.configuration.api_key['Authorization'] = 'token=' + os.environ['onfido_token']
onfido.configuration.api_key_prefix['Authorization'] = 'Token'
api = onfido.DefaultApi()

test_applicant_id = '65e42db1-3132-46ba-9ece-371cf1823b16'

live_videos = api.list_live_videos(test_applicant_id).live_videos

print(live_videos)

download = api.download_live_video(live_videos[0].id)
