Python - NETCONF-table-to-dictionary
====================================

A function that takes NETCONF GetReplys and converts a specified table to a dictionary of rows

This Python function takes in XML and irrelevant of namespaces returns children of elements based on entry key and row match.
Acknowledge this routine is for gathering children from an element. If all of the data you require is in this:
<data>blah</data> format, then this will not work. if however your data looks like directly below, then you're in luck!

<stuff>
    <data>blah</data>
        <interface>
            <name>dave</name>
            <speed>depends on beer/sleep ratio</speed>
            <happy>mostly</happy>
        </interface>
        <interface>
            <name>david</name>
            <status>meh</status>
        </interface>
</stuff>
 
In this case: tkey='data' and tvalue='blah', ROW_FORMAT= 'interface'
You could also do this: tkey='stuff', tvalue=None, ROW_FORMAT='interface'
 
Entry Key: This is the point at which the _loop_counterator reaches and start's 'looking' for the row keys.
Row Keys: This is the row tag which contains children elements which will be added into a dictionary within a 'row' construct. 
Returns: a Dictionary of dictionaries.