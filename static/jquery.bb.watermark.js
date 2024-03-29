﻿/* jquery.bb.watermark.js
* BradBamford's Easy Watermark v1.0
* Date: Wed Mar 09 21:23:05 2010 -0500

* Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
* 
* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
* DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
* USE OR OTHER DEALINGS IN THE SOFTWARE.

*/
(function ($) {
	$.fn.watermark = function (options) {

		var defaults = {
			text: null,
			color: "#cccccc",
			fontSize: ".875em",
			top: "1px",
			left: "5px",
			className: "watermark"
		};

		return this.filter('input:text').each(function () {
			defaults.text = $(this).attr("title");

			settings = $.extend({}, defaults, options);

			var wrapper$ = $("<span />", { "style": "position:relative" });
			$(this).after(wrapper$).detach().appendTo(wrapper$);

			var watermark$ = $("<label />", { "text": settings.text, "for": $(this).attr("id"), "class": settings.className });
			watermark$.css({
				"position": "absolute",
				"top": settings.top,
				"left": settings.left,
				"z-index": "1",
				"color": settings.color,
				"font-size": settings.fontSize				
			});
			watermark$.appendTo(wrapper$);

			$(this).focus(function () {
				if (this.value == "") { watermark$.hide(); }
			});

			$(this).blur(function () {
				if (this.value == '') { watermark$.show(); }
			});

			if (!$(this).val() == "") { watermark$.hide(); }

		});
	};
})(jQuery);