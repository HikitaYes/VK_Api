import requests, sys


class Program:
    def __init__(self, id):
        self.id = id
        self.token = '&v=5.107&access_token=bf347b91bf347b91bf347b91bfbf460fd1bbf34bf347b91e1ef2831f5802102261a409f'

    def find(self):
        queryUser = f'https://api.vk.com/method/users.get?user_ids={self.id}{self.token}&fields=bdate,followers_count'
        self.get_info_user(queryUser)
        queryPhotos = f'https://api.vk.com/method/photos.getAlbums?owner_id={self.id}{self.token}'
        self.get_info_albums(queryPhotos)
        queryFriends = f'https://api.vk.com/method/friends.get?user_id={self.id}{self.token}&fields=nickname'
        self.get_info_friends(queryFriends)

    def get_info_user(self, query):
        user = None
        try:
            user = requests.get(query)
        except requests.HTTPError as e:
            print('Error connection: ', e)
        data = user.json()['response'][0]
        self.id = data['id']
        print(f'Name: {data["first_name"]} {data["last_name"]}')
        if data['is_closed']:
            print('Account is closed')
            sys.exit()
        print(f'Birth Date: {data["bdate"]}')
        print(f'Followers count {data["followers_count"]}\n')

    def get_info_albums(self, query):
        user = None
        try:
            user = requests.get(query)
        except requests.HTTPError as e:
            print('Error connection: ', e)
        data = user.json()['response']
        print('Number of albums: ', data['count'])
        for album in data['items']:
            print(album['title'])
        print('\n')

    def get_info_friends(self, query):
        user = None
        try:
            user = requests.get(query)
        except requests.HTTPError as e:
            print('Error connection: ', e)
        data = user.json()['response']
        print('Number of friends: ', data['count'])
        for friend in data['items']:
            print(f'Name: {friend["first_name"]} {friend["last_name"]}, id: {friend["id"]}')
        print('\n')

if __name__ == '__main__':
    print('Enter user\'s id')
    id = input()
    p = Program(id)
    p.find()