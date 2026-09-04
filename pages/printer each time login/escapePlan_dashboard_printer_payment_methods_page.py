from playwright.sync_api import Page


class PrinterPaymentMethodsPage:
    def __init__(self, page: Page):
        self.page = page

        self.settings_link = page.get_by_role(
            "link",
            name="Settings"
        )

        self.payment_methods_button = page.get_by_role(
            "button",
            name="Payment Methods Cards & bank"
        )

        # Stripe iframe
        self.stripe_frame = page.frame_locator(
            # 'iframe[name^="__privateStripeFrame"]'
             'iframe[title="Secure card payment input frame"]'
        )

        self.card_number_input = self.stripe_frame.get_by_role(
            "textbox",
            name="Credit or debit card number"
        )

        self.expiry_input = self.stripe_frame.get_by_role(
            "textbox",
            name="Credit or debit card expiration date"
        )

        self.cvc_input = self.stripe_frame.get_by_role(
            "textbox",
            name="Credit or debit card CVC/CVV"
        )

        self.zip_input = self.stripe_frame.get_by_role(
            "textbox",
            name="ZIP"
        )

        self.add_card_button = page.get_by_role(
            "button",
            name="Add Card"
        )

        self.setup_payouts_button = page.get_by_role(
            "button",
            name="Set Up Payouts with Stripe"
        )

    def click_settings(self) -> None:
        self.settings_link.click()

    def open_payment_methods(self) -> None:
        self.payment_methods_button.click()

    def enter_card_number(self, card_number: str) -> None:
        self.card_number_input.fill(card_number)

    def enter_expiry(self, expiry: str) -> None:
        self.expiry_input.fill(expiry)

    def enter_cvc(self, cvc: str) -> None:
        self.cvc_input.fill(cvc)

    def enter_zip(self, zip_code: str) -> None:
        self.zip_input.fill(zip_code)

    def click_add_card(self) -> None:
        self.add_card_button.click()

    def click_setup_payouts(self) -> None:
        self.setup_payouts_button.click()

    def add_card(
        self,
        card_number: str,
        expiry: str,
        cvc: str,
        zip_code: str,
    ) -> None:
        self.click_settings()
        self.open_payment_methods()

        self.enter_card_number(card_number)
        self.enter_expiry(expiry)
        self.enter_cvc(cvc)
        self.enter_zip(zip_code)

        self.click_add_card()

    def setup_stripe_payouts(self) -> None:
        self.click_setup_payouts()