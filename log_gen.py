import random
import string


d = {
  "index_patterns": "nginx_json_elastic",
  "settings": {
    "index.refresh_interval": "5s"
  },
  "mappings": {
    "doc": {
      "dynamic_templates": [
        {
          "message_field": {
            "mapping": {
              "norms": 0,
              "type": "text"
            },
            "match_mapping_type": "string",
            "match": "message"
          }
        },
        {
          "string_fields": {
            "mapping": {
              "type": "text",
              "norms": 0,
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            },
            "match_mapping_type": "string",
            "match": "*"
          }
        }
      ],
      "properties": {
        "geoip": {
          "dynamic": 0,
          "properties": {
            "location": {
              "type": "geo_point"
            }
          },
          "type": "object"
        },
        "request": {
          "type": "keyword"
        }
      }
    }
  }
}

d2 = {
    "level": "info",
    "information":{
        "here": 1,
        "there": 100
    }
}

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(8)

for i in range(10):
    d["random"] = get_random_string(10)
    d2["random_2"] = get_random_string(12)
    print(d)



