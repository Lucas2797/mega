


{
    console.log('{{name}}')
    const cacheName = 'cache-v1';
    const resourcesToPrecache = [
        "{% url 'home' %}",
        "{% url 'sw.js' %}",
        "{% url 'install_sw' %}",
        "{% url 'manifestjson' %}",
        "{% url 'test_amp' %}",
        "{% url 'test' %}",
        "{% url 'contact' %}",
    ];

    self.addEventListener('install', function (event) {
        console.log('sw install event!');
        event.waitUntil(
            caches.open(cacheName)
                .then(function (cache) {
                    console.log('cache added')
                    return cache.addAll(resourcesToPrecache);
                }
                )
        );
    });

    self.addEventListener('fetch', function (event) {
        console.log(event.request.url);

        event.respondWith(
            caches.match(event.request).then(function (response) {
                return response || fetch(event.request);
            })
        );
    });
};

console.log('ok')






// importScripts('https://cdn.ampproject.org/sw/amp-sw.js');
// AMP_SW.init({
//     assetCachingOptions: [{
//         regexp: /\.(png|jpg)/,
//         cachingStrategy: 'CACHE_FIRST'
//     }],
//     offlinePageOptions: {
//         url: "{% url 'home' %}",
//         assets: []
//     }
// });

// console.log('ok')