'''
Created on 20 Oct 2014

@author: davidgee

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
'''

from lxml import etree

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# Test Data

test_data = """<?xml version="1.0" encoding="ISO-8859-1"?>
<rpc-reply xmlns:vlan_mgr_cli="http://www.cisco.com/nxos:1.0:vlan_mgr_cli" xmlns:nfcli="http://www.cisco.com/nxos:1.0:nfcli" xmlns:nxos="http://www.cisco.com/nxos:1.0" xmlns:if="http://www.cisco.com/nxos:1.0:if_manager" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:mod="http://www.cisco.com/nxos:1.0:urib" message-id="urn:uuid:a7f23575-5f56-11e4-b260-7831c1bd1cf4">
  <data>
    <mod:show>
      <mod:__XML__BLK_Cmd_urib_show_routing_command_routing>
        <mod:__XML__OPT_Cmd_urib_show_routing_command_vrf>
          <mod:__XML__OPT_Cmd_urib_show_routing_command_ip>
            <mod:ip/>
          </mod:__XML__OPT_Cmd_urib_show_routing_command_ip>
        </mod:__XML__OPT_Cmd_urib_show_routing_command_vrf>
        <mod:ip>
          <mod:route/>
        </mod:ip>
        <mod:__XML__OPT_Cmd_urib_show_routing_command_vrf>
          <mod:__XML__OPT_Cmd_urib_show_routing_command_ip>
            <mod:__XML__OPT_Cmd_urib_show_routing_command_unicast>
              <mod:__XML__OPT_Cmd_urib_show_routing_command_topology>
                <mod:__XML__OPT_Cmd_urib_show_routing_command_l3vm-info>
                  <mod:__XML__OPT_Cmd_urib_show_routing_command_rpf>
                    <mod:__XML__OPT_Cmd_urib_show_routing_command_ip-addr>
                      <mod:__XML__OPT_Cmd_urib_show_routing_command_protocol>
                        <mod:__XML__OPT_Cmd_urib_show_routing_command_summary>
                          <mod:__XML__OPT_Cmd_urib_show_routing_command_vrf>
                            <mod:__XML__OPT_Cmd_urib_show_routing_command___readonly__>
                              <mod:__readonly__>
                                <mod:TABLE_vrf>
                                  <mod:ROW_vrf>
                                    <mod:vrf-name-out>default</mod:vrf-name-out>
                                    <mod:TABLE_addrf>
                                      <mod:ROW_addrf>
                                        <mod:addrf>ipv4</mod:addrf>
                                        <mod:TABLE_prefix>
                                          <mod:ROW_prefix>
                                            <mod:ipprefix>0.0.0.0/0</mod:ipprefix>
                                            <mod:ucast-nhops>1</mod:ucast-nhops>
                                            <mod:mcast-nhops>0</mod:mcast-nhops>
                                            <mod:attached>true</mod:attached>
                                            <mod:TABLE_path>
                                              <mod:ROW_path>
                                                <mod:uptime>PT1H57M50S</mod:uptime>
                                                <mod:pref>1</mod:pref>
                                                <mod:metric>0</mod:metric>
                                                <mod:clientname>static</mod:clientname>
                                                <mod:ubest>true</mod:ubest>
                                              </mod:ROW_path>
                                            </mod:TABLE_path>
                                          </mod:ROW_prefix>
                                          <mod:ROW_prefix>
                                            <mod:ipprefix>192.168.10.0/24</mod:ipprefix>
                                            <mod:ucast-nhops>1</mod:ucast-nhops>
                                            <mod:mcast-nhops>0</mod:mcast-nhops>
                                            <mod:attached>true</mod:attached>
                                            <mod:TABLE_path>
                                              <mod:ROW_path>
                                                <mod:ipnexthop>192.168.10.222</mod:ipnexthop>
                                                <mod:ifname>Eth2/4</mod:ifname>
                                                <mod:uptime>PT1H57M50S</mod:uptime>
                                                <mod:pref>0</mod:pref>
                                                <mod:metric>0</mod:metric>
                                                <mod:clientname>direct</mod:clientname>
                                                <mod:ubest>true</mod:ubest>
                                              </mod:ROW_path>
                                            </mod:TABLE_path>
                                          </mod:ROW_prefix>
                                          <mod:ROW_prefix>
                                            <mod:ipprefix>192.168.10.222/32</mod:ipprefix>
                                            <mod:ucast-nhops>1</mod:ucast-nhops>
                                            <mod:mcast-nhops>0</mod:mcast-nhops>
                                            <mod:attached>true</mod:attached>
                                            <mod:TABLE_path>
                                              <mod:ROW_path>
                                                <mod:ipnexthop>192.168.10.222</mod:ipnexthop>
                                                <mod:ifname>Eth2/4</mod:ifname>
                                                <mod:uptime>PT1H57M50S</mod:uptime>
                                                <mod:pref>0</mod:pref>
                                                <mod:metric>0</mod:metric>
                                                <mod:clientname>local</mod:clientname>
                                                <mod:ubest>true</mod:ubest>
                                              </mod:ROW_path>
                                            </mod:TABLE_path>
                                          </mod:ROW_prefix>
                                          <mod:ROW_prefix>
                                            <mod:ipprefix>192.168.11.0/24</mod:ipprefix>
                                            <mod:ucast-nhops>1</mod:ucast-nhops>
                                            <mod:mcast-nhops>0</mod:mcast-nhops>
                                            <mod:attached>true</mod:attached>
                                            <mod:TABLE_path>
                                              <mod:ROW_path>
                                                <mod:uptime>PT1H57M50S</mod:uptime>
                                                <mod:pref>1</mod:pref>
                                                <mod:metric>0</mod:metric>
                                                <mod:clientname>static</mod:clientname>
                                                <mod:ubest>true</mod:ubest>
                                              </mod:ROW_path>
                                            </mod:TABLE_path>
                                          </mod:ROW_prefix>
                                          <mod:ROW_broken>
                                            <mod:ipprefix>1.1.1.0/24</mod:ipprefix>
                                            <mod:ucast-nhops>99</mod:ucast-nhops>
                                            <mod:mcast-nhops>99</mod:mcast-nhops>
                                            <mod:attached>ERROR</mod:attached>
                                          </mod:ROW_broken>
                                        </mod:TABLE_prefix>
                                      </mod:ROW_addrf>
                                    </mod:TABLE_addrf>
                                  </mod:ROW_vrf>
                                </mod:TABLE_vrf>
                              </mod:__readonly__>
                            </mod:__XML__OPT_Cmd_urib_show_routing_command___readonly__>
                          </mod:__XML__OPT_Cmd_urib_show_routing_command_vrf>
                        </mod:__XML__OPT_Cmd_urib_show_routing_command_summary>
                      </mod:__XML__OPT_Cmd_urib_show_routing_command_protocol>
                    </mod:__XML__OPT_Cmd_urib_show_routing_command_ip-addr>
                  </mod:__XML__OPT_Cmd_urib_show_routing_command_rpf>
                </mod:__XML__OPT_Cmd_urib_show_routing_command_l3vm-info>
              </mod:__XML__OPT_Cmd_urib_show_routing_command_topology>
            </mod:__XML__OPT_Cmd_urib_show_routing_command_unicast>
          </mod:__XML__OPT_Cmd_urib_show_routing_command_ip>
        </mod:__XML__OPT_Cmd_urib_show_routing_command_vrf>
      </mod:__XML__BLK_Cmd_urib_show_routing_command_routing>
    </mod:show>
  </data>
</rpc-reply>
"""

cmd_clear_mac_address = "clear mac address-table dynamic address %s"

#--------------------------------------------------------------------------------------------------------------------------------------------------------

def return_table(raw, tkey, tvalue, ROW_FORMAT):
    """
    return_table(raw, TABLE_FORMAT, ROW_FORMAT)
        raw = raw NETCONF test data
        tkey = table key
        tvalue = table value
            These two take some explaining. Why did I opt to do this?
            Well given this was written in anger to deal with a networking issue, I might want to
            grab data from a specific set of tables within the XML if it's a large data set.
            tkey could equal something like 'addrf' or 'TABLE_prefix'. It means you can match on a parent element or
            set an entry point for a tag that has data and no children.
            tvalue is the text if it's something like addrf below. See the __main__ routine for usage of examples.
            
        ROW_FORMAT = row entry point - what _rows should you be grabbing the children from?
        
        
    This routine returns a dict of dicts
    """

    _rows = {}
    _loop_counter = 0
    _temp_dict = {}
    _table_key_dict = { tkey : tvalue }
    _element_entry_point = []
    _end_rows = {}
    debug = False

    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.XML(str(raw), parser)
    for el in root.iter('*'):
        # Seach element.tag and element.text here for things like: addrf = ipv4
        
        if (("{" or "}") in str(el.tag)):
            _start = el.tag.find("}")
            _temp_dict[el.tag[_start+1:]] = el.text
                    
        elif (("{" or "}") not in str(el.tag)):
            _temp_dict[el.tag] = el.text
        
        # OK HIT THIS:
        
        try:
            if _table_key_dict.keys() == _temp_dict.keys() and _table_key_dict.values() == _temp_dict.values():
                if debug:
                    print "FOUND TABLE INSERT POINT"
                # Set the external_element reference to 'el' so it doesn't break the _loop_counterator
                _element_entry_point = el
                break
        except:
            pass
        
        _temp_dict= {}
    

    # If our search failed, just return empty else it will cause other parsing issues
    if _element_entry_point == []:
        return _rows
 
    # T__rows = _rows in the TABLE
    # For ROW in TABLE[X]
    root = etree.XML(str(raw), parser)
    root.find(str(_element_entry_point))
    for el in root.iter('*'):
        # Seach element.tag and element.text here for things like: addrf = ipv4
        if (("{" or "}") in str(el.tag)):
            _start = el.tag.find("}")
            _temp_dict[el.tag[_start+1:]] = el.text
                    
        elif (("{" or "}") not in str(el.tag)):
            _temp_dict[el.tag] = el.text
        
        if _temp_dict.has_key(ROW_FORMAT):
            if debug:
                print "FOUND ROW_FORMAT"
            # NOW Let's load a dictionary with each row
            _end_rows[_loop_counter] = list(el)
            if debug:
                print "FORMED _end_rows[%s]" % str(_loop_counter)
            _loop_counter += 1
        _temp_dict = {}
    
    for ele in _end_rows:

        # Actual _rows we're interested in
        for each in _end_rows[ele]:
            for el in each.iter('*'):
                
                if (("{" or "}") in str(el.tag)):
                    _start = el.tag.find("}")
                    _temp_dict[el.tag[_start+1:]] = el.text
                    
                elif (("{" or "}") not in str(el.tag)):
                    _temp_dict[el.tag] = el.text
            

        _rows[_loop_counter] = _temp_dict
        _temp_dict = {}
        _loop_counter += 1
        
    return _rows

#----------------- MAIN ENTRY POINT ---------------
if __name__ == '__main__':
    
    # Create Dictionary ready for output
    table_result = {}
    
    # Using our test data, send the data and the TABLE_ENTRY_POINT and ROW_ENTRY_POINT to 'return_table(data, TABLE_FORMAT, ROW_FORMAT)'
    table_result = return_table(test_data,"addrf", "ipv4", "ROW_prefix")
    
    print "TEST 1"    
    for each in table_result:
        print table_result[each]
        
    table_result = return_table(test_data,"TABLE_prefix", None, "ROW_prefix")    
    
    print "TEST 2"
    for each in table_result:
        print table_result[each]  
    
