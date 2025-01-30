"use strict"

ckan.module('preview_image', function($) {
    return {
        initialize: function() {
            $.proxyAll(this, /_on/);
            console.log(this.el.prop('files'))
            console.log('initializing preview image module ...')
            
            this.el.on('change', this._onChange);
        },

        _onChange: function(event) {
            console.log(this.el)
            const files = this.el.prop('files');
            // console.log(this.el.prop('files'))
            if (files) {
                console.log(files)
                const fileReader = new FileReader();

                const imgContainer = document.getElementById('imgPreviewContainer');

                fileReader.onload = event => {
                    imgContainer.setAttribute('src', event.target.result);
                }

                fileReader.readAsDataURL(files[0])
            }
            else {
                console.log('element tidak ditemukan')
            }
        }
    };
});