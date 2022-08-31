class Payment(models.Model):
    def __init__(self) -> None:
        super().__init__()
        self.is_paid = models.BooleanField(default=False)
        self.payment_agent = models.CharField(max_length=30)    


    def conclude_payment(self):
        self.is_paid = True

    def set_payment_agent(self, provider): 
        self.payment_agent = provider

    def is_payment_open(self):
        return not self.is_paid

    def check_provider_availability(provider, provider_type = None):
        if provider_type:
            return provider.filter(type=provider_type).count()
        else:
            provider.count()


    payment_agents = {
        "Provider_1": "Provider1" ,
        "Provider_2": "AO Provider2",
        "Provider_3": "Provider 3",
        "Provider_4": "Complex Provider 4 Name With Surname",
        "Provider_5": "Provider5 Full Company-Name",
    }

    def update_payment_agent(self):
        if self.check_provider_availability(self.provider1, 1):
            self.set_payment_agent(self.payment_agents["Provider_1"])

        elif self.check_provider_availability(self.provider2, 1):
            self.set_payment_agent(self.payment_agents["Provider_2"])

        elif self.check_provider_availability(self.provider3, 1):
            self.set_payment_agent(self.payment_agents["Provider_3"])

        elif self.check_provider_availability(self.provider4):
            self.set_payment_agent(self.payment_agents["Provider_4"])

        else:
            self.set_payment_agent(self.payment_agents["Provider_5"])

        self.save()

    def get_payment_agent(self):
        U"""
        A monkey patch to get payment agent. Now is it store in the special field in the database. This method is deprecated and is used for backwards compatibility.

        .. deprecated:: r574
        """
        if self.is_payment_open():
            return U"-"
        else:
            return self.payment_agent

