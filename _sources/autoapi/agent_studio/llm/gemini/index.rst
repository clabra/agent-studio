:py:mod:`agent_studio.llm.gemini`
=================================

.. py:module:: agent_studio.llm.gemini


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.llm.gemini.GeminiProvider




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.llm.gemini.config
   agent_studio.llm.gemini.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: GeminiProvider(**kwargs)


   Bases: :py:obj:`agent_studio.llm.base_model.BaseModel`

   .. py:attribute:: name
      :value: 'gemini'

      

   .. py:method:: compose_messages(intermedia_msg: list[dict[str, Any]]) -> Any


   .. py:method:: generate_response(messages: list[dict[str, Any]], **kwargs) -> tuple[str, dict[str, int]]

      Creates a chat completion using the Gemini API.



