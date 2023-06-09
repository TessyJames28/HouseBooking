from django.shortcuts import render, redirect
# from .forms import AgentRegForm, AgentRegForm2
from.models import Agent
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class AgentCreate(CreateView):
    model = Agent

class AgentUpdate(UpdateView):
    model = Agent

# def agent_registration(request):
#     form = AgentRegForm()
#     if request.method == "POST":
#         form = AgentRegForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, "agent_reg.html", context)

# def agent_registration2(request, agent_id):
#     agent = AgentReg.objects.get(agent_id=agent_id)
#     if request.method == "POST":
#         form = AgentRegForm2(request.POST, request.FILES)
#         if form.is_valid():
#            agent_reg2 = form.save(commit=False)
#            agent_reg2.agent = agent
#            agent_reg2.save()
#            return redirect('success_page')
#     else:
#         form = AgentRegForm2()
#     context = {
#         'agent': agent,
#         'form': form
#     }
#     return render(request, "agent_reg2.html", context)

# # def document_list(request):
# #     documents = AgentReg2.objects.all()
# #     return render(request, "agent_doc_list.html", {'documents': documents})
