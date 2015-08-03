import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json
    else:
        r.raise_for_status


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    # results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    results = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
    # print len(results['artist']),
    # print (results['artist'][0].keys())
    # pretty_print(results['artist'])
    count = 0
    for index in range(len(results['artist'])):
        # print results['artist'][index]['name'].strip().lower()
        if results['artist'][index]['name'].strip().lower() == "FIRST AID KIT".lower():
           count = count + 1
    # print count 
    
    # Begin Area for Queen
    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")    
    print results['artist'][0]['begin-area']['name']
        
        
    # name of the alias for BEATLES in Spain    
    results = query_by_name(ARTIST_URL, query_type["simple"], "BEATLES")
    aliases = results['artist'][0]['aliases']
    for a in aliases:
        if a['locale'] == 'es':
           print a['name'] 
     
    # Nirvana diambiguation       
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")         
    print results['artist'][0]['disambiguation']  
    
    # When was One Direction formed?
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    print results['artist'][0]['life-span']['begin']  

    artist_id = results["artist"][1]["id"]
    print "\nARTIST:"
    pretty_print(results["artist"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    print "\nONE RELEASE:"
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]

    print "\nALL TITLES:"
    for t in release_titles:
        print t


if __name__ == '__main__':
    main()