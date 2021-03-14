//edit AllowList for special HTML in popover
const myDefaultAllowList = bootstrap.Tooltip.Default.allowList
// To allow button elements with onclick
myDefaultAllowList.button = ["onclick"]
myDefaultAllowList.textarea = ["cols", "rows", "wrap", "readonly", "style", "onclick"]

// activate popovers
const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
const popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
})

