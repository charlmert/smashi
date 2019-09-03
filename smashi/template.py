import os
from . import file

templateString = '91e7c34f01c8a8177cdeac699c17faeb_TEMPLATE_STRING'
literalTemplateString = 'c26a290da61cef0df960d25819af04d7_LITERAL_TEMPLATE_STRING'

"""
    Save transformed template to the file specified by path
"""
def text(self, text, variables, path):
    transformed = text.replace('{', '{{').replace('}', '}}').replace('%s', templateString).replace('%', '%%').replace(templateString, '%s') % variables
    os.makedirs('%s' % (os.path.dirname(path)), exist_ok=True)
    smashi.file.create('%s' % (path), transformed)
    return transformed

"""
    Save transformed template from the file specified by templateFile to the
    file specified by path
"""
def file(self, templateFile, variables, path):
    with open('%s' % (templateFile), 'r') as fp:
        text = fp.read()
        # parsing escapes \%s
        transformed = text.replace('\\%s', literalTemplateString)
        # more string formatting literals
        transformed = transformed.replace('{', '{{').replace('}', '}}').replace('%s', templateString).replace('%', '%%').replace(templateString, '%s')
        transformed = transformed % variables

        # put literal escapes back %s now.
        transformed = transformed.replace(literalTemplateString, '%s')
        # string formatting literals back as well
        transformed = transformed.replace('{{', '{').replace('}}', '}').replace('%%', '%')

        os.makedirs('%s' % (os.path.dirname(path)), exist_ok=True)
        smashi.file.create('%s' % (path), transformed)
        return transformed
    return False
