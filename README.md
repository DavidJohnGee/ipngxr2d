Python---NETCONF-table-to-dictionary
====================================

A function that takes NETCONF GetReplys and converts a specified table to a dictionary of rows

'return_table(raw, TABLE_FORMAT, ROW_FORMAT)' takes:
  raw = NETCONF GetReply
  TABLE_FORMAT = a string that represents what the table entry point looks like (see included test data in the source)
  ROW_FORMAT = a string that represents what the desired rows look like (see included test data in the source)
  returns a dictionary of rows
  
    
    table_result = return_table(test_data,"TABLE_prefix","ROW_prefix")

    print "========== ROWS RETURNED =========="
    for each in table_result:
        print table_result[each]
    
    # For each row, use some of the data and make it human readable
    print "\n========== PRETTY PRINT ========== "
    for each in table_result:
        print "PREFIX: " + str(table_result[each].get("ipprefix")) + " NEXT-HOP " + str(table_result[each].get("ipnexthop")) 
