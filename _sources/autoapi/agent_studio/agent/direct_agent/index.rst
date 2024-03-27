:py:mod:`agent_studio.agent.direct_agent`
=========================================

.. py:module:: agent_studio.agent.direct_agent


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.agent.direct_agent.DirectAgent




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.agent.direct_agent.config
   agent_studio.agent.direct_agent.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: DirectAgent(model: agent_studio.llm.base_model.BaseModel)


   Bases: :py:obj:`agent_studio.agent.base_agent.BaseAgent`

   Zero-shot LLM agents.

   .. py:attribute:: name
      :type: str
      :value: 'direct'

      

   .. py:method:: reset(instruction: str) -> None


   .. py:method:: trajectory2intermediate_msg() -> list[dict[str, Any]]

      Converts the trajectory to intermediate messages.

      :returns:

                The intermediate messages.
                    + role:
                        - system
                        - user
                        - assistant
                    + content: The content of the message.                    content can either be a string or a np.array.                    If it is a np.array, it should be in RGB format.
      :rtype: list[dict[str, Any]]


   .. py:method:: eval(final_obs: numpy.ndarray | None = None) -> dict[str, Any]



