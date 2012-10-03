# -*- coding: utf-8 -*-
from django.conf import settings
from django.forms.widgets import TextInput
from django.utils.safestring import SafeUnicode

try:
    url = settings.STATIC_URL
except AttributeError:
    try:
        url = settings.MEDIA_URL
    except AttributeError:
        url = ''

class ColorFieldWidget(TextInput):
    class Media:
        css = {
            'all': ("%scolorful/css/colorpicker.css" % url, )
        }
        js  = ("%scolorful/js/colorpicker.js" % url, )

    input_type = 'color'

    def render_script(self, id, value):
        rgv_val = ", ".join([x+y for x,y in zip(['r:','g:','b:'], value.split(','))]) if value else ''
        return u'''<script type="text/javascript">
                    (function($){
                        $(document).ready(function(){

                            $('#%(id)s').each(function(i, elm){
                                $(this).ColorPicker({
                                    color: {%(value)s },
                                    onShow: function (colpkr) {
                                        $(colpkr).fadeIn(500);
                                        return false;
                                    },
                                    onHide: function (colpkr) {
                                        $(colpkr).fadeOut(500);
                                        return false;
                                    },
                                    onChange: function (hsb, hex, rgb) {
                                        //$('#colorSelector div').css('backgroundColor', '#' + hex);
                                        //console.log(rgb);
                                        $('#%(id)s').val(rgb.r+', '+rgb.g+', '+rgb.b);
                                    }
                                });
                            });


                            $('#%(id)s').each(function(i, elm){
                                // Make sure html5 color element is not replaced
                                if (elm.type != 'color') $(elm).ColorPicker();
                            });
                        });
                    })('django' in window ? django.jQuery: jQuery);
                </script>
                ''' % {'id': id, 'value': rgv_val}

    def render(self, name, value, attrs={}):
        if not 'id' in attrs:
            attrs['id'] = "#id_%s" % name
        render = super(ColorFieldWidget, self).render(name, value, attrs)
        return SafeUnicode(u"%s%s" % (render, self.render_script(attrs['id'], value)))
