"use strict";

Array.from(document.getElementsByClassName("yt_images")).forEach(function (item) {
    const imageHeight = item.naturalHeight;
    const imageWidth = item.naturalWidth;

    const htmlString = `
    <div class="text-center">
    <small>Original image height: ${imageHeight}px. Original image width:  ${imageWidth}px</small>
    </div>
    `;

    item.insertAdjacentHTML("afterend", htmlString);

});