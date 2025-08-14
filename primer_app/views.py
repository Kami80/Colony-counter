import openai
from django.shortcuts import render
from django.conf import settings
from .forms import PrimerInputForm

# Add your OpenAI API key to settings.py
openai.api_key = settings.OPENAI_API_KEY

def design_primer(request):
    if request.method == "POST":
        form = PrimerInputForm(request.POST)
        if form.is_valid():
            target_sequence = form.cleaned_data['target_sequence']
            primer_length = form.cleaned_data['primer_length']
            tm = form.cleaned_data['tm']
            gc_content = form.cleaned_data['gc_content']
            product_size = form.cleaned_data['product_size']
            
            # Send request to OpenAI
            prompt = f"Design a genomic primer for the following sequence:\n\n{target_sequence}\n\n"
            prompt += f"Primer Length: {primer_length}\nTm: {tm}°C\nGC Content: {gc_content}%\nProduct Size: {product_size} bp"

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI."},
                    {"role": "user", "content": prompt},
                ]
            )

            designed_primers = response['choices'][0]['message']['content']
            
            return render(request, 'primer_app/result.html', {'primers': designed_primers})
    else:
        form = PrimerInputForm()

    return render(request, 'primer_app/design_primer.html', {'form': form})
