import labeler

@admin.register(MyModel)
class MyAdmin(admin.ModelAdmin):
    """ Tag Model needs a color and name attribute """

    def attr_to_label(obj):
        tags = obj.mytags.all()
        return mark_safe(labeler(tags))

    list_display = ('pk', attr_to_label)
