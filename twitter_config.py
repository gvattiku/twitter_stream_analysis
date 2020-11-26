import pickle

twitter = {"api_key": "ROTea2fY3pU5X9aUWhXSpXjpp",
           "api_secret": "WFl8MJJmfMMcGk13Q1NDqduxew6Kul2HddmpvDMGzVX6u4U8yq",
           "bearer_token": "AAAAAAAAAAAAAAAAAAAAABBZKAEAAAAAkvmC88oToeC3eMANgWwS946umnY%3DA9mKaijPbEagvVaht09DLxLOb2A04NrmNG6Rw0Tf1ubhLI8B6G"}

pickle.dump(twitter, open("config.p", "wb"))