# rmp_query

Simple script to query a server in the RAGE:MP masterlist.  
Clone this repository using `git clone https://github.com/dalhy/rmp_query.git`.

## Querying
    from rmp_query import Querier
    # import querier
    data = Querier("127.0.0.1", port=22005).info()
    # give address and port as parameters to Querier instance, if address is None, then the Querier will try to find server using the 22005 port