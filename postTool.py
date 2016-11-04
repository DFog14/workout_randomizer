import datetime, xmlrpclib, time, json

def config_parse():
    with open('config.json') as json_file:
        data = json.load(json_file)
    return data['wordpress']['url'], data['wordpress']['username'], data['wordpress']['password'], data['wordpress']['blogid']

def post(content, categories):
    url, username, password, blogid = config_parse()
    date = time.strftime("%Y-%m-%d")
    clock = time.strftime(" %H:%M")

    status_draft = 0
    status_published = 1

    server = xmlrpclib.ServerProxy(url)

    title = "Hotto's Workout. Week: {}".format(date) 
    date_created = xmlrpclib.DateTime(datetime.datetime.strptime(date + clock, "%Y-%m-%d %H:%M"))
    tags = [""]
    data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags}
    post_id = server.metaWeblog.newPost(blogid, username, password, data, status_published)

def main():
    post("Test", ["Workout"])

#main()
