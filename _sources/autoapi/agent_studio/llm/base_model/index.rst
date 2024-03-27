:py:mod:`agent_studio.llm.base_model`
=====================================

.. py:module:: agent_studio.llm.base_model


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.llm.base_model.BaseModel




.. py:class:: BaseModel


   Base class for models.

   .. py:attribute:: name
      :type: str
      :value: 'base'

      

   .. py:method:: compose_messages(intermediate_msg: list[dict[str, Any]]) -> Any
      :abstractmethod:


   .. py:method:: generate_response(messages: list[dict[str, Any]], **kwargs) -> tuple[str, dict[str, int]]
      :abstractmethod:

      Generate a response given messages.



