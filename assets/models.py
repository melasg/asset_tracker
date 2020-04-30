from django.db import models
from datetime import date
from django.core.validators import validate_ipv4_address

class Vendor(models.Model):
	vendor_name = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.vendor_name

	class Meta:
		verbose_name = 'Vendor'
		verbose_name_plural = 'Vendors'

class Asset(models.Model):
	name = models.CharField(max_length=30, unique=True)
	active = models.BooleanField(default=True)
	asset_type = models.CharField(max_length=30,default='',blank=True,choices=[
                                                                ('ASSET','Asset'),
                                                                ('HARDWARE','Hardware'),
                                                                ('SOFTWARE','Software'),
                                                                ('SYSTEM','System'),
                                                                ('SWITCH','Switch'),
                                                                ('CLUST','Clust')])

	vendor_char = models.CharField(max_length=50,blank=True)
	vendor = models.ManyToManyField(Vendor,blank=True)
	contract_start = models.DateField(default=date.today,blank=True)
	contract_end = models.DateField(default=date.today,blank=True)
	received_date = models.DateField(default=date.today,blank=True)
	link_to_pdf = models.CharField(max_length=2048,default='',blank=True)
	order_number = models.CharField(max_length=30,default='',blank=True)
	quote = models.CharField(max_length=20,default='',blank=True)
	account = models.CharField(max_length=50,default='',blank=True)
	owner = models.CharField(max_length=50,default='',blank=True)
	customer_PO = models.CharField(max_length=20,default='',blank=True)
	comments = models.TextField(default='',blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Asset'
		verbose_name_plural = 'Assets'

class Hardware(Asset):
	property_id = models.IntegerField(default=0,blank=True)
	location = models.CharField(max_length=30,default='Genomics 1120A')
	serial_number = models.CharField(max_length=30,default='',blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = 'Hardware'

class Software(Asset):
	vendor_customer_number = models.CharField(max_length=30,default='',blank=True)
	quantity = models.IntegerField(default=0,blank=True)
	part_number = models.CharField(max_length=30,default='',blank=True)
	description = models.TextField(default='',blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = 'Software'

class Component(models.Model):
	name = models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Component'
		verbose_name_plural = 'Components'

class System(Hardware):
	IP = models.CharField(max_length=30,default='',unique=True, validators=[validate_ipv4_address],blank=True)
	MAC_address = models.CharField(max_length=50,default='',unique=True)
	CPU_cores = models.CharField(max_length=5,default='',blank=True)
	memory_GB = models.CharField(max_length=10,default='',blank=True)
	primary_disk_size_GB = models.CharField(max_length=10,default='',blank=True)
	watts = models.CharField(max_length=10,default='',blank=True)
	component_char = models.CharField(max_length=50,default='',blank=True)
	component = models.ManyToManyField(Component,blank=True)
	component_quantity = models.IntegerField(default=0,blank=True)

	def __str_(self):
		return self.name

	class Meta:
		verbose_name = 'System'
		verbose_name_plural = 'Systems'

class Switch(Hardware):
	ETHERNET_1Gb = 'ETH 1Gb'
	ETHERNET_10Gb = 'ETH 10Gb'
	INFINIBAND = 'IB'
	TYPE_CHOICES = ((ETHERNET_1Gb, 'Ethernet 1Gb'),(ETHERNET_10Gb, 'Ethernet 10Gb'),(INFINIBAND, 'Infiniband'))
	switch_type = models.CharField(max_length=8,choices=TYPE_CHOICES,default='',blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Switch'
		verbose_name_plural = 'Switches'

#class Drive(Hardware):
#class Tray(Hardware):
class Partition(models.Model):
	partition = models.CharField(max_length=50,default='',blank=True)

	def __str__(self):
		return self.partition

	class Meta:
		verbose_name = 'Partition'
		verbose_name_plural = 'Partitions'

class Clust(System):
	partition_char = models.CharField(max_length=50,default='',blank=True)
	partition = models.ManyToManyField(Partition,blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = verbose_name_plural = 'Clust'
