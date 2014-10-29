'''
Created on 29 Oct 2014

@author: davidgee
'''

import sys
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
#--------------------------------------------------------------------------------------------------------------------------------------------------------

def return_table(raw, TABLE_FORMAT, ROW_FORMAT):
    """
    return_table(raw, TABLE_FORMAT, ROW_FORMAT)
        raw = raw NETCONF data that excludes garbage - see test data
        TABLE_FORMAT = table entry point - what table do you want to take the rows from?
        ROW_FORMAT = row entry point - what rows should you be reading from?
        
        Note - there isn't boundary checking. If there are different types of ROWs in a table type (unlikely)
        ROW data may be malformed as it will be included through the loop.
        
    This routine returns a dict of dicts
    """
    
    TABLE_FOUND = False
    ROW = []
    ROWS = {}
    ROWS2 = {}
    IN_ROW = False
    ROW_ITER = -1
    DICTO = {}
    
    try:
        parser = etree.XMLParser(remove_blank_text=True)
        root = etree.XML(str(raw), parser)
        for el in root.iter('*'):
            processed = False 
            if TABLE_FOUND:
                
                if ROW_FORMAT in str(el):
                    IN_ROW = True
                    
                if IN_ROW == True:
                    if ROW_FORMAT in str(el):
                        ROW_ITER += 1
                        if "[]" not in str(ROW):
                            ROWS[ROW_ITER] = ROW
                            ROWS2[ROW_ITER] = DICTO
                            ROW = []
                            DICTO = {}
                    if ROW_FORMAT not in str(el):
                        
                        if (("{" or "}") in str(el.tag)):
                            _start = el.tag.find("}")
                            RDATA = { el.tag[_start+1:] : el.text }
                            DICTO[el.tag[_start+1:]] = el.text
                            ROW.append(RDATA)
                        
                        elif (("{" or "}") not in str(el.tag)):
                            RDATA = { el.tag : el.text }
                            DICTO[el.tag] = el.text
                            ROW.append(RDATA)
                            
                        
                    
            if TABLE_FORMAT in str(el):
                TABLE_FOUND = True
        
        ROW_ITER += 1
        ROWS[ROW_ITER] = ROW
        ROWS2[ROW_ITER] = DICTO
    except:
        print "Something went wrong!: {0}".format(sys.exc_info()[0])
    return ROWS2

#----------------- MAIN ENTRY POINT ---------------
if __name__ == '__main__':
    
    # Create Dictionary ready for output
    table_result = {}
    
    # Using our test data, send the data and the TABLE_ENTRY_POINT and ROW_ENTRY_POINT to 'return_table(data, TABLE_FORMAT, ROW_FORMAT)'
    table_result = return_table(test_data,"TABLE_prefix","ROW_prefix")
    
    # Print the returned data
    print "========== ROWS RETURNED =========="
    for each in table_result:
        print table_result[each]
    
    # For each row, use some of the data and make it human readable
    print "\n========== PRETTY PRINT ========== "
    for each in table_result:
        print "PREFIX: " + str(table_result[each].get("ipprefix")) + " NEXT-HOP " + str(table_result[each].get("ipnexthop")) 
