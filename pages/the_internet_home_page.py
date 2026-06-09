from .base_page import BasePage
from .ab_test_page import ABTestPage
from .add_remove_elements_page import AddRemoveElementsPage
from .basic_auth_page import BasicAuthPage
from .broken_images_page import BrokenImagesPage
from .challenging_dom_page import ChallengingDOMPage
from .checkboxes_page import CheckboxesPage
from .context_menu_page import ContextMenuPage
from .digest_auth_page import DigestAuthPage
from .disappearing_elements_page import DisappearingElementsPage
from .drag_and_drop_page import DragAndDropPage
from .dropdown_page import DropdownPage
from .dynamic_content_page import DynamicContentPage
from .dynamic_controls_page import DynamicControlsPage
from .dynamic_loading_page import DynamicLoadingPage
from .entry_ad_page import EntryAdPage
from .exit_intent_page import ExitIntentPage
from .file_download_page import FileDownloadPage
from .file_upload_page import FileUploadPage
from .floating_menu_page import FloatingMenuPage
from .forgot_password_page import ForgotPasswordPage
from .form_authentication_page import FormAuthenticationPage
from .frames_page import FramesPage
from .geolocation_page import GeolocationPage
from .horizontal_slider_page import HorizontalSliderPage
from .hovers_page import HoversPage
from .infinite_scroll_page import InfiniteScrollPage
from .inputs_page import InputsPage
from .jquery_ui_menus_page import JQueryUIMenusPage
from .javascript_alerts_page import JavaScriptAlertsPage
from .javascript_error_page import JavaScriptErrorPage
from .key_presses_page import KeyPressesPage
from .large_deep_dom_page import LargeDeepDOMPage
from .multiple_windows_page import MultipleWindowsPage
from .nested_frames_page import NestedFramesPage
from .notification_message_page import NotificationMessagePage
from .redirect_link_page import RedirectLinkPage
from .secure_file_download_page import SecureFileDownloadPage
from .shadow_dom_page import ShadowDOMPage
from .shifting_content_page import ShiftingContentPage
from .slow_resources_page import SlowResourcesPage
from .sortable_data_tables_page import SortableDataTablesPage
from .status_codes_page import StatusCodesPage
from .typos_page import TyposPage
from .wysiwyg_editor_page import WysiwygEditorPage


class TheInternetHomePage(BasePage):
    def click_ab_testing(self) -> ABTestPage:
        self.click_link("A/B Testing")
        return ABTestPage(self.page, self.page.url)

    def click_add_remove_elements(self) -> AddRemoveElementsPage:
        self.click_link("Add/Remove Elements")
        return AddRemoveElementsPage(self.page, self.page.url)

    def click_basic_auth(self) -> BasicAuthPage:
        self.click_link("Basic Auth")
        return BasicAuthPage(self.page, self.page.url)

    def click_broken_images(self) -> BrokenImagesPage:
        self.click_link("Broken Images")
        return BrokenImagesPage(self.page, self.page.url)

    def click_challenging_dom(self) -> ChallengingDOMPage:
        self.click_link("Challenging DOM")
        return ChallengingDOMPage(self.page, self.page.url)

    def click_checkboxes(self) -> CheckboxesPage:
        self.click_link("Checkboxes")
        return CheckboxesPage(self.page, self.page.url)

    def click_context_menu(self) -> ContextMenuPage:
        self.click_link("Context Menu")
        return ContextMenuPage(self.page, self.page.url)

    def click_digest_auth(self) -> DigestAuthPage:
        self.click_link("Digest Authentication")
        return DigestAuthPage(self.page, self.page.url)

    def click_disappearing_elements(self) -> DisappearingElementsPage:
        self.click_link("Disappearing Elements")
        return DisappearingElementsPage(self.page, self.page.url)

    def click_drag_and_drop(self) -> DragAndDropPage:
        self.click_link("Drag and Drop")
        return DragAndDropPage(self.page, self.page.url)

    def click_dropdown(self) -> DropdownPage:
        self.click_link("Dropdown")
        return DropdownPage(self.page, self.page.url)

    def click_dynamic_content(self) -> DynamicContentPage:
        self.click_link("Dynamic Content")
        return DynamicContentPage(self.page, self.page.url)

    def click_dynamic_controls(self) -> DynamicControlsPage:
        self.click_link("Dynamic Controls")
        return DynamicControlsPage(self.page, self.page.url)

    def click_dynamic_loading(self) -> DynamicLoadingPage:
        self.click_link("Dynamic Loading")
        return DynamicLoadingPage(self.page, self.page.url)

    def click_entry_ad(self) -> EntryAdPage:
        self.click_link("Entry Ad")
        return EntryAdPage(self.page, self.page.url)

    def click_exit_intent(self) -> ExitIntentPage:
        self.click_link("Exit Intent")
        return ExitIntentPage(self.page, self.page.url)

    def click_file_download(self) -> FileDownloadPage:
        self.click_link("File Download")
        return FileDownloadPage(self.page, self.page.url)

    def click_file_upload(self) -> FileUploadPage:
        self.click_link("File Upload")
        return FileUploadPage(self.page, self.page.url)

    def click_floating_menu(self) -> FloatingMenuPage:
        self.click_link("Floating Menu")
        return FloatingMenuPage(self.page, self.page.url)

    def click_forgot_password(self) -> ForgotPasswordPage:
        self.click_link("Forgot Password")
        return ForgotPasswordPage(self.page, self.page.url)

    def click_form_authentication(self) -> FormAuthenticationPage:
        self.click_link("Form Authentication")
        return FormAuthenticationPage(self.page, self.page.url)

    def click_frames(self) -> FramesPage:
        self.click_link("Frames")
        return FramesPage(self.page, self.page.url)

    def click_geolocation(self) -> GeolocationPage:
        self.click_link("Geolocation")
        return GeolocationPage(self.page, self.page.url)

    def click_horizontal_slider(self) -> HorizontalSliderPage:
        self.click_link("Horizontal Slider")
        return HorizontalSliderPage(self.page, self.page.url)

    def click_hovers(self) -> HoversPage:
        self.click_link("Hovers")
        return HoversPage(self.page, self.page.url)

    def click_infinite_scroll(self) -> InfiniteScrollPage:
        self.click_link("Infinite Scroll")
        return InfiniteScrollPage(self.page, self.page.url)

    def click_inputs(self) -> InputsPage:
        self.click_link("Inputs")
        return InputsPage(self.page, self.page.url)

    def click_jquery_ui_menus(self) -> JQueryUIMenusPage:
        self.click_link("JQuery UI Menus")
        return JQueryUIMenusPage(self.page, self.page.url)

    def click_javascript_alerts(self) -> JavaScriptAlertsPage:
        self.click_link("JavaScript Alerts")
        return JavaScriptAlertsPage(self.page, self.page.url)

    def click_javascript_error(self) -> JavaScriptErrorPage:
        self.click_link("JavaScript onload event error")
        return JavaScriptErrorPage(self.page, self.page.url)

    def click_key_presses(self) -> KeyPressesPage:
        self.click_link("Key Presses")
        return KeyPressesPage(self.page, self.page.url)

    def click_large_deep_dom(self) -> LargeDeepDOMPage:
        self.click_link("Large & Deep DOM")
        return LargeDeepDOMPage(self.page, self.page.url)

    def click_multiple_windows(self) -> MultipleWindowsPage:
        self.click_link("Multiple Windows")
        return MultipleWindowsPage(self.page, self.page.url)

    def click_nested_frames(self) -> NestedFramesPage:
        self.click_link("Nested Frames")
        return NestedFramesPage(self.page, self.page.url)

    def click_notification_message(self) -> NotificationMessagePage:
        self.click_link("Notification Messages")
        return NotificationMessagePage(self.page, self.page.url)

    def click_redirect_link(self) -> RedirectLinkPage:
        self.click_link("Redirect Link")
        return RedirectLinkPage(self.page, self.page.url)

    def click_secure_file_download(self) -> SecureFileDownloadPage:
        self.click_link("Secure File Download")
        return SecureFileDownloadPage(self.page, self.page.url)

    def click_shadow_dom(self) -> ShadowDOMPage:
        self.click_link("Shadow DOM")
        return ShadowDOMPage(self.page, self.page.url)

    def click_shifting_content(self) -> ShiftingContentPage:
        self.click_link("Shifting Content")
        return ShiftingContentPage(self.page, self.page.url)

    def click_slow_resources(self) -> SlowResourcesPage:
        self.click_link("Slow Resources")
        return SlowResourcesPage(self.page, self.page.url)

    def click_sortable_data_tables(self) -> SortableDataTablesPage:
        self.click_link("Sortable Data Tables")
        return SortableDataTablesPage(self.page, self.page.url)

    def click_status_codes(self) -> StatusCodesPage:
        self.click_link("Status Codes")
        return StatusCodesPage(self.page, self.page.url)

    def click_typos(self) -> TyposPage:
        self.click_link("Typos")
        return TyposPage(self.page, self.page.url)

    def click_wysiwyg_editor(self) -> WysiwygEditorPage:
        self.click_link("WYSIWYG Editor")
        return WysiwygEditorPage(self.page, self.page.url)
