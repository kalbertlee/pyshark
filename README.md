# PyShark
Wireshark with Python
## 功能
* 实现scapy对pcap文件解析
* 实现wireshark的过滤器操作
* 实现过滤器历史记录，方便二次查询

## 过滤器
1. 字段搜索
2. 字符搜索
3. 流跟踪 [ip.src port.src ip.dst port.dst] 构成索引

## 数据库表
* pcap包列表 pcap_list
* pcap包解析结果 pcap_result < pcap_list
* pcap过滤器操作 pcap_filter < pcap_list
* pcap过滤器操作结果 pcap_filter_result < pcap_filter
* pcap流跟踪 pcap_tcpstream/pcap_udpstream < pcap_list

## 页面
3. 
2.
1.