// MIT Licensed
// Author: jwilson8767

/**
 * Waits for an element satisfying selector to exist, then resolves promise with the element.
 * Useful for resolving race conditions.
 *
 * @param selector
 * @returns {Promise}
 */
function elementReady(selector) {
  return new Promise((resolve, reject) => {
    let el = document.querySelector(selector);
    if (el) {resolve(el);}
    new MutationObserver((mutationRecords, observer) => {
      // Query for elements matching the specified selector
      Array.from(document.querySelectorAll(selector)).forEach((element) => {
        resolve(element);
        //Once we have resolved we don't need the observer anymore.
        observer.disconnect();
      });
    })
      .observe(document.documentElement, {
        childList: true,
        subtree: true
      });
  });
}
// -- end of licence --


// not working
elementReady("#textToCopy").then(() => setTimeout(focusText, 10))

function focusText() {
    const node = "textToCopy"
    /* Get the text field */
    const copyText = document.getElementById(node);

    /* Scroll the text field */
    copyText.scrollLeft = copyText.scrollWidth;

    console.log("Focussed the text")
}

function copyToClipboard() {
    /* Get the text field */
    const copyText = document.getElementById("textToCopy");

    /* Select the text field */
    copyText.focus();
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    document.execCommand("copy");

    /* Alert the copied text */
    alert("Copied link to clipboard!");
}