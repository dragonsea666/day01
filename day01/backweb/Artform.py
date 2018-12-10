



from django import forms

class AddArtForm(forms.Form):
    title = forms.CharField(min_length=4, required=True,
                            error_messages={
                                'required':'文章标题是必填项',
                                'min_length':'文章标题不能小于5字符'
                            }
                            )
    describe = forms.CharField(min_length=10, required=True,
                           error_messages={
                               'required': '文章简短描述是必填项',
                               'min_length': '文章简短描述不能小于20字符'
                           }
                           )
    content = forms.CharField(required=True)

    titlepic = forms.ImageField(required=True, error_messages={
        'required':'首图必填'
    })

    keywords = forms.CharField(min_length=2, required=True, error_messages={
        'required': '关键字是必填项',
        'min_length': '关键字述不能小于2字符'
    })

    category = forms.CharField(min_length=2, required=True, error_messages={
        'required': '文章分类是必填项',
        'min_length': '文章分类字数不能小于2字符'
    })

class EditArtForm(forms.Form):
    title = forms.CharField(min_length=4, required=True,
                            error_messages={
                                'required': '文章标题是必填项',
                                'min_length': '文章标题不能小于4字符'
                            }
                            )
    describe = forms.CharField(min_length=10, required=True,
                               error_messages={
                                   'required': '文章简短描述是必填项',
                                   'min_length': '文章简短描述不能小于10字符'
                               }
                               )
    content = forms.CharField(required=True)

    titlepic = forms.ImageField(required=False)

    keywords = forms.CharField(min_length=2, required=True, error_messages={
        'required': '关键字是必填项',
        'min_length': '关键字述不能小于2字符'
    })

    category = forms.CharField(min_length=2, required=False, error_messages={
        'required': '文章分类是必填项',
        'min_length': '文章分类字数不能小于2字符'
    })