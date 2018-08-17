"use strict";

window.addEventListener('load', function () {

    Array.from(document.getElementsByClassName("yt_images")).forEach(function (item) {
        const imageHeight = item.naturalHeight;
        const imageWidth = item.naturalWidth;
        const src = item.src;

        const htmlString = `
    <div class="text-center" style="overflow-wrap: break-word;">
    <small><a href="${src}">${src}</a></small><br>
    <small>Original image height: ${imageHeight}px. Original image width:  ${imageWidth}px</small>
    </div>
    `;

        item.insertAdjacentHTML("afterend", htmlString);

    });

});