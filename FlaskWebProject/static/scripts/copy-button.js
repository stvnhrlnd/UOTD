(function () {
    var copyButton = new Clipboard('#copy-button');
    var copyButtonLabel = document.getElementById('copy-button-label');

    copyButton.on('success', function (e) {
        var innerHTML = copyButtonLabel.innerHTML;
        copyButtonLabel.innerHTML = 'Copied';

        setTimeout(function () {
            copyButtonLabel.innerHTML = innerHTML;
        }, 2000);
    });
}());