from django import forms

CONTACT_ISSUE_CHOICES = [
    ('general_support', 'Support and General Enquiries'),
    ('purchase_issue', 'Unable to Purchase'),
    ('billing_issue', 'Credit Card Billing Issue'),
    ('technical_issue', 'Technical Issue'),
    ('follow_up', 'Follow up on return/refund'),
    ('suggestions', 'Suggestions and Ideas'),
]


class ContactUsForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    reason = forms.CharField(label='Reason', widget=forms.Select(choices=CONTACT_ISSUE_CHOICES))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
