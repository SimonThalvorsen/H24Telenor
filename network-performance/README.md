# Mobile Network Performance

Statistikk fra Ookla Speedtest for bedre innblikk i kundenes opplevde hastighet i mobilnettet

Vi har hentet ut ca ett år med filer (ca 500 000 rader data) som vi ønsker at dere skal analysere og gjerne finne noe 
om mobilnettet vårt som kan være nyttig for å forbedre kundeopplevelsen
Mulige teknologier: 
- Python med numpy, Matlab eller et annet ønsket språk.

Åpent for å skrive kode og gjennomføre en analyse, eller komme med en mer konseptuell plan for analyse.
Vurderingen legger vekt på gode ideer og kreativitet, det er ikke nødvendig å ha den mest komplekse koden. 

Det er vedlagt en PDF-fil med informajon om feltene.  

Feltnavene: 
- id_result
- guid_result
- id_platform
- ts_result
- ts_result_received
- attr_location_timezone
- id_device
- attr_device_android_fingerprint
- attr_device_model
- attr_device_manufacturer
- attr_device_model_raw
- attr_device_manufacturer_raw
- attr_device_brand_raw
- attr_device_chipset
- attr_device_chipset_manufacturer
- attr_device_hardware_name
- attr_device_os_version
- attr_device_build
- is_device_rooted
- attr_device_radio
- attr_device_ram_mb
- attr_device_storage_mb
- is_device_world_phone
- attr_device_multi_sim_support
- num_device_active_modems
- num_device_supported_modems
- is_device_concurrent_voice_data_supported
- is_device_data_connection_allowed
- is_device_data_capable
- is_device_data_roaming_enabled
- is_device_icc_card_present
- attr_device_service_state
- attr_device_thermal_status
- val_device_thermal_headroom
- is_app_permission_phone_state
- is_app_permission_fine_location
- is_app_permission_coarse_location
- is_app_permission_background_location
- is_app_permission_wifi_state
- attr_sim_operator_common_name
- attr_sim_operator_name_raw
- attr_sim_operator_mcc
- attr_sim_operator_mnc
- attr_altsim_operator_name
- attr_altsim_operator_mcc
- attr_altsim_operator_mnc
- attr_network_operator_mcc
- attr_network_operator_mnc
- attr_network_operator_common_name
- attr_isp_common_name
- attr_isp_name_raw
- attr_sim_type_allocation_code
- attr_sim_state
- attr_test_method
- attr_test_ip_version
- id_connection_type_start
- id_connection_type_end
- num_connections_failed
- is_connection_carrier_aggregation
- attr_connection_nr_state
- attr_connection_apn
- id_connection_net_speed
- is_connection_access_technology_nr
- id_connection_network_override_type
- attr_connection_downstream_bandwidth_kbps
- attr_connection_upstream_bandwidth_kbps
- attr_connection_nat64_prefix
- attr_location_latitude
- attr_location_longitude
- attr_location_start_latitude
- attr_location_start_longitude
- id_location_start_type
- id_location_end_type
- attr_location_accuracy_m
- attr_location_age_ms
- attr_location_altitude_m
- attr_location_vertical_accuracy_m
- attr_location_speed_mps
- attr_place_formatted_address
- attr_place_name
- attr_place_locality_type
- attr_place_country
- attr_place_country_code
- attr_place_region
- attr_place_subregion
- attr_place_subsubregion
- attr_place_postal_code
- num_packet_loss_sent
- num_packet_loss_received
- metric_packet_loss_percent
- is_download_stopped
- val_latency_min_ms
- val_latency_iqm_ms
- val_latency_max_ms
- val_multiserver_latency_ms
- val_download_latency_min_ms
- val_download_latency_iqm_ms
- val_download_latency_max_ms
- val_upload_latency_min_ms
- val_upload_latency_iqm_ms
- val_upload_latency_max_ms
- num_traceroute_hops
- attr_traceroute0_ip_address
- val_traceroute0_latency_ms
- attr_traceroute1_ip_address
- val_traceroute1_latency_ms
- val_jitter_ms
- val_multiserver_jitter_ms
- val_download_kbps
- val_test_download_kb
- num_test_download_threads
- val_test_download_duration_ms
- val_upload_kbps
- val_test_upload_kb
- num_test_upload_threads
- val_test_upload_duration_ms
- attr_network_ipv4_address
- attr_network_ipv6_address
- attr_network_asn
- attr_app_version
- attr_app_store
- attr_server_name
- attr_server_sponsor_name
- attr_server_latitude
- attr_server_longitude
- val_server_distance_km
- attr_server_country
- attr_server_country_code
- is_server_auto_selected
- is_server_on_network
- attr_server_asn
- num_server_download
- val_signal_rsrp_dbm
- val_signal_csi_rsrp_dbm
- val_signal_ss_rsrp_dbm
- val_signal_rsrq_db
- val_signal_csi_rsrq_db
- val_signal_ss_rsrq_db
- val_signal_rssnr_db
- val_signal_csi_snr_db
- val_signal_ss_snr_db
- val_signal_wcdma_ecno_db
- val_signal_rssi_dbm
- val_signal_gsm_rssi_dbm
- val_signal_timing_advance_ts
- val_signal_cqi
- attr_cell_nr_frequency_range
- attr_cell_bandwidth_khz
- attr_cell_bandwidths_khz
- id_cell_primary
- id_cell_lte_enodeb
- attr_cell_pci
- attr_cell_nr_pci
- attr_cell_tac
- attr_cell_lac
- attr_cell_psc
- attr_cell_frequency_channel
- attr_cell_frequency_channel_type
- attr_cell_nr_arfcn
- attr_cell_lte_bands
- attr_cell_nr_bands
- is_network_roaming
- is_network_international_roaming
- is_network_vpn
- is_device_5g_capable
- attr_connection_type_start_string
- attr_connection_type_end_string
- attr_device_esim_embedded
- id_cell_nr
- id_cell_start
- attr_network_operator_mcc_nr
- attr_network_operator_mnc_nr