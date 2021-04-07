# Anagram

### Posting data in json format

`$ curl localhost:5000/load -d '["foobar", "aabb", "barfoo", "baba", "boofar", "test"]' -H 'Content-Type: application/json' -X PUT`

### Getting the anagrams
```
$ curl 'localhost:5000/get?word=foobar'
$ curl 'localhost:5000/get?word=abab'
```
