from django.contrib import admin
from .models import Asset, Hardware, Software, System, Switch, Clust, Component, Vendor, Partition
from import_export import resources
from import_export.admin import ImportExportModelAdmin

'''
<Asset Type>Admin(...) Handles whats displayed on the admin page for each type
<Asset Type>Resource(...) Handles the import/export feature of each type
'''

'''---------------------------------------------'''

class AssetAdmin(admin.ModelAdmin):
	search_fields = ('name','active', 'order_number', 'customer_PO', 'account', 'owner')
	list_display = ('name', 'active', 'contract_end')
	list_filter = ('active', 'asset_type', 'vendor', 'owner', 'account')
	fieldsets = (('General Information', {
			'fields': ('name', 'active', 'asset_type', 'vendor', 'contract_start', 'contract_end', 
				'received_date', 'link_to_pdf', 'order_number', 'quote', 'account', 'owner',
				'customer_PO', 'comments')}),)

'''-----------------------------------------------'''

class HardwareResource(resources.ModelResource):

	class Meta:
		model = Hardware
		exclude = ('asset_ptr',)

class HardwareAdmin(AssetAdmin, ImportExportModelAdmin):
	search_fields = AssetAdmin.search_fields + ('property_id', 'location', 'serial_number')
	list_filter = AssetAdmin.list_filter + ('location',)
	fieldsets = AssetAdmin.fieldsets + (('Hardware Information', {
			'fields': ('property_id', 'location', 'serial_number')}),)
	resource_class = HardwareResource

'''------------------------------------------------'''

class SoftwareResource(resources.ModelResource):

	class Meta:
		model = Software
		exclude = ('asset_ptr',)

class SoftwareAdmin(AssetAdmin, ImportExportModelAdmin):
	search_fields = AssetAdmin.search_fields + ('part_number', 'vendor_customer_number')
	fieldsets = AssetAdmin.fieldsets + (('Software Information', {
			'fields': ('vendor_customer_number', 'quantity', 'part_number', 'description')}),)
	resource_class = SoftwareResource

'''-------------------------------------------------'''

class SystemResource(resources.ModelResource):

	class Meta:
		model = System
		exclude = ('hardware_ptr', 'asset_ptr')

class SystemAdmin(HardwareAdmin,ImportExportModelAdmin):
	search_fields = HardwareAdmin.search_fields + ('IP', 'MAC_address')
	list_filter = HardwareAdmin.list_filter + ('component',)
	fieldsets = HardwareAdmin.fieldsets + (('System Information', {
			'fields': ('IP', 'MAC_address', 'CPU_cores', 'memory_GB', 'primary_disk_size_GB', 'watts', 'component', 'component_quantity')}),)
	resource_class = SystemResource

'''-----------------------------------------------------'''

class SwitchResource(resources.ModelResource):

	class Meta:
		model = Switch
		exclude = ('hardware_ptr', 'asset_ptr')

class SwitchAdmin(HardwareAdmin, ImportExportModelAdmin):
	search_fields = HardwareAdmin.search_fields + ('switch_type',)
	list_filter = HardwareAdmin.list_filter + ('switch_type',)
	fieldsets = HardwareAdmin.fieldsets + (('Switch Information', {
			'fields': ('switch_type',)}),)
	resource_class = SwitchResource

'''------------------------------------------------------'''

class ClustResource(resources.ModelResource):

	class Meta:
		model = Clust
		exclude = ('system_ptr', 'hardware_ptr', 'asset_ptr')

class ClustAdmin(SystemAdmin, ImportExportModelAdmin):
	list_filter = SystemAdmin.list_filter + ('partition',)
	fieldsets = SystemAdmin.fieldsets + (('Clust Information', {
			'fields': ('partition',)}),)
	resource_class = ClustResource

'''------------------------------------------------------'''

class ComponentAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	list_filter = ('name',)
	fieldsets = (('Component Information', {
			'fields': ('name',)}),)

'''-------------------------------------------------------'''

class VendorAdmin(admin.ModelAdmin):
	search_fields = ('vendor_name',)
	list_filter = ('vendor_name',)
	fieldsets = (('Vendor Information', {
			'fields': ('vendor_name',)}),)

'''--------------------------------------------------------'''

class PartitionAdmin(admin.ModelAdmin):
	search_fields = ('partition',)
	list_filter = ('partition',)
	fieldsets = (('Partition Information', {
		'fields': ('partition',)}),)

admin.site.register(Asset, AssetAdmin)
admin.site.register(Hardware, HardwareAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Clust, ClustAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Partition, PartitionAdmin)
