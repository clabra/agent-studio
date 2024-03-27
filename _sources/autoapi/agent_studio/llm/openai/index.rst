:py:mod:`agent_studio.llm.openai`
=================================

.. py:module:: agent_studio.llm.openai


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.llm.openai.OpenAIProvider




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.llm.openai.config
   agent_studio.llm.openai.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: OpenAIProvider(**kwargs: Any)


   Bases: :py:obj:`agent_studio.llm.base_model.BaseModel`

   Base class for models.

   .. py:attribute:: name
      :value: 'openai'

      

   .. py:method:: compose_messages(intermedia_msg: list[dict[str, Any]]) -> list[dict[str, Any]]

      Composes the messages to be sent to the model.


   .. py:method:: generate_response(messages: list[dict[str, Any]], **kwargs) -> tuple[str, dict[str, int]]

      Creates a chat completion using the OpenAI API.



