# src/logic/span/span/computer.py

"""
Module: logic.span.span.computer
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

from logic.coord import Coord, CoordService
from logic.span import (
    DiagonalRayProvider, NoRayProviderException, PerpendicularRayProvider, Span, SpanComputationException,
    SpanComputationRouteException, SpannerEngineException
)
from logic.system import ComputationResult, LoggingLevelRouter


class SpannerEngine:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def compute(
            cls,
            origin: Coord,
            coord_service: CoordService = CoordService(),
            diagonal_ray_provider: Optional[DiagonalRayProvider] = None,
            perpendicular_ray_provider: Optional[PerpendicularRayProvider] = None,
    ):
        """
        Action:
            1.  Send an exception chain in the ComputationResult if
                    *   The origin is not certified as a safe coord.
                    *   No ray provider is included.
            2.  If both diagonal and perpendicular ray providers are included route production to
                _compute_queen_span.
            3.  Otherwise, route to either _compute_rook_span or _compute_bishop_span.
            
        Args:
            origin: Coord
            coord_service: CoordService
            diagonal_ray_provider: Optional[DiagonalRayProvider]
            perpendicular_ray_provider: Optional[PerpendicularRayProvider]
            
        Returns:
            ComputationResult[Span]
            
        Raises:
            SpannerEngineException
            SpanComputationException
            NoRayProviderException
            
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, no ray_provider is included.
        providers = (diagonal_ray_provider, perpendicular_ray_provider)
        if len(providers) == 0:
            # Send the exception on failure.
            return ComputationResult.failure(
                SpannerEngineException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SpannerEngineException.MSG,
                    err_code=SpannerEngineException.ERR_CODE,
                    ex=SpanComputationException(
                        mthd=method,
                        op=SpanComputationException.OP,
                        msg=SpanComputationException.MSG,
                        err_code=SpanComputationException.ERR_CODE,
                        rslt_type=SpanComputationException.RSLT_TYPE,
                        ex=NoRayProviderException(
                        msg=NoRayProviderException.MSG,
                        err_code=NoRayProviderException.ERR_CODE
                        )
                    )
                )
            )
        # Handle the case that, the origin is not certified as a safe coord.
        origin_validation = coord_service.validator.validate(candidate=origin)
        if origin_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                SpannerEngineException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SpanComputationException.MSG,
                    err_code=SpannerEngineException.ERR_CODE,
                    ex=SpanComputationException(
                        mthd=method,
                        op=SpanComputationException.OP,
                        msg=SpanComputationException.MSG,
                        err_code=SpanComputationException.ERR_CODE,
                        rslt_type=SpanComputationException.RSLT_TYPE,
                        ex=origin_validation.exception
                    )
                )
            )
        # --- Route to the appropriate computation logic. ---#
        
        # Get a queen's span if perpendicular and diagonal providers are included.
        if diagonal_ray_provider is not None and perpendicular_ray_provider is not None:
            return cls._compute_queen_span(
                origing=origin,
                coord_service=coord_service,
                diagonal_provider=diagonal_ray_provider,
                perpendicular_provider=perpendicular_ray_provider
            )
        # Get a bishop's span if only a diagonal provider exists
        if diagonal_ray_provider is not None:
            return cls._compute_bishop_span(
                origin=origin,
                coord_service=coord_service,
                provider=diagonal_ray_provider
            )
        # Get a rook's span if only a perpendicular provider exists
        if perpendicular_ray_provider is not None:
            return cls._compute_rook_span(
                origin=origin,
                coord_service=coord_service,
                provider=perpendicular_ray_provider
            )
        # Handle the default case that no solution logic exists for a provider combination.
        return ComputationResult.failure(
            SpannerEngineException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=SpanComputationException.MSG,
                err_code=SpannerEngineException.ERR_CODE,
                ex=SpanComputationException(
                    mthd=method,
                    op=SpanComputationException.OP,
                    msg=SpanComputationException.MSG,
                    err_code=SpanComputationException.ERR_CODE,
                    rslt_type=SpanComputationException.RSLT_TYPE,
                    ex=SpanComputationRouteException(
                        msg=SpanComputationRouteException.MSG,
                        err_code=SpanComputationRouteException.ERR_CODE,
                    )
                )
            )
        )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_queen_span(
            cls,
            origin,
            coord_service: CoordService,
            diagonal_provider: DiagonalRayProvider,
            perpendicular_provider: PerpendicularRayProvider
    ) -> ComputationResult[Span]:
        """
        Action:
            1.  Get the diagonal component of the queen's span by calling _compute_bishop_span.
            2.  If the diagonal span is not computed, send an exception chain in the ComputationResult.
                Else, use the _compute_rook_span to get the queen's perpendicular span.
            3.  If the perpendicular span is not computed, send an exception chain in the ComputationResult.
            4.  Append the perpendicular span's rays to the diagonal span's rays to get the quent's entire span.
            5.  Send the Queen's span in the ComputationResult.
            
        Args:
            origin: Coord
            coord_service: CoordService
            diagonal_provider: DiagonalRayProvider
            perpendicular_provider: PerpendicularRayProvider
            
        Returns:
            ComputationResult[Span]
        
        Raises:
            SpannerEngineException
            SpanComputationException
        """
        method = f"{cls.__name__}._compute_queen_span"
        
        # --- Compute the queen's diagonal span. ---#
        diagonal_span_result = cls._compute_bishop_span(
            origin=origin,
            coord_service=coord_service,
            diagonal_provider=diagonal_provider,
        )
        # Handle the case that, the queen's diagonal span is not computed.
        if diagonal_span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                SpannerEngineException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SpanComputationException.MSG,
                    err_code=SpannerEngineException.ERR_CODE,
                    ex=SpanComputationException(
                        mthd=method,
                        op=SpanComputationException.OP,
                        msg=SpanComputationException.MSG,
                        err_code=SpanComputationException.ERR_CODE,
                        rslt_type=SpanComputationException.RSLT_TYPE,
                        ex=diagonal_span_result.exception
                    )
                )
            )
        # --- Compute the queen's perpendicular span. ---#
        perpendicular_span_result = cls._compute_rook_span(
            origin=origin,
            coord_service=coord_service,
            perpendicular_provider=perpendicular_provider,
        )
        # Handle the case that, the rook span is not computed.
        if perpendicular_span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                SpannerEngineException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SpanComputationException.MSG,
                    err_code=SpannerEngineException.ERR_CODE,
                    ex=SpanComputationException(
                        mthd=method,
                        op=SpanComputationException.OP,
                        msg=SpanComputationException.MSG,
                        err_code=SpanComputationException.ERR_CODE,
                        rslt_type=SpanComputationException.RSLT_TYPE,
                        ex=perpendicular_span_result.exception
                    )
                )
            )
        # --- Add the perpendicular and diagonal components to ge the queen's entire span. ---#
        queen_span = Span(origin=origin, rays=[])
        for ray in diagonal_span_result.payload.rays:
            queen_span.rays.append(ray)
        # Perpendicular rays next.
        for ray in perpendicular_span_result.payload.rays:
            queen_span.rays.append(ray)
        
        # --- Send the success result to the caller. ---#
        return ComputationResult.success(queen_span)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_bishop_span(
            cls,
            origin,
            coord_service: CoordService,
            provider: DiagonalRayProvider,
    ) -> ComputationResult[Span]:
        """
        Action:
            1.  Iterate through the provider's factors to compute each ray. If the ray is not computed, send
                an exception chain in the ComputationResult. Else, include the ray in the span.
            2.  Return the computed span when the loop is complete.

        Args:
            origin: Coord
            coord_service: CoordService
            provider: DiagonalRayProvider

        Returns:
            ComputationResult[Span]

        Raises:
            SpannerEngineException
            SpanComputationException
        """
        method = f"{cls.__name__}._bishop_span"
        
        # --- Add the computed ray to the span. ---#
        span = Span(origin=origin, rays=[])
        for factor in provider.factors.to_list:
            ray_result = provider.ray.compute(
                origin=origin,
                factor=factor,
                coord_service=coord_service
            )
           # Handle the case that, the rook span is not computed.
            if ray_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    SpannerEngineException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SpanComputationException.MSG,
                        err_code=SpannerEngineException.ERR_CODE,
                        ex=SpanComputationException(
                            mthd=method,
                            op=SpanComputationException.OP,
                            msg=SpanComputationException.MSG,
                            err_code=SpanComputationException.ERR_CODE,
                            rslt_type=SpanComputationException.RSLT_TYPE,
                            ex=ray_result.exception
                        )
                    )
                )
            # Add the ray to its span.
            if ray_result.payload not in span.rays:
                span.rays.append(ray_result.payload)
            
        # --- Send the success result to the caller. ---#
        return ComputationResult.success(span)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_rook_span(
            cls,
            origin,
            coord_service: CoordService,
            provider: PerpendicularRayProvider
    ) -> ComputationResult[Span]:
        """
        Action:
            1.  Iterate through the provider's factors to compute each ray. If the ray is not computed, send
                an exception chain in the ComputationResult. Else, include the ray in the span.
            2.  Return the computed span when the loop is complete.

        Args:
            origin: Coord
            coord_service: CoordService
            provider: PerpendicularRayProvider

        Returns:
            ComputationResult[Span]

        Raises:
            SpannerEngineException
            SpanComputationException
        """
        method = f"{cls.__name__}._rook_span"
        
        # --- Add the computed ray to the span. ---#
        span = Span(origin=origin, rays=[])
        for factor in provider.factors.to_list:
            ray_result = provider.ray.compute(
                origin=origin,
                factor=factor,
                coord_service=coord_service
            )
            # Handle the case that, the rook span is not computed.
            if ray_result.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    SpannerEngineException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SpanComputationException.MSG,
                        err_code=SpannerEngineException.ERR_CODE,
                        ex=SpanComputationException(
                            mthd=method,
                            op=SpanComputationException.OP,
                            msg=SpanComputationException.MSG,
                            err_code=SpanComputationException.ERR_CODE,
                            rslt_type=SpanComputationException.RSLT_TYPE,
                            ex=ray_result.exception
                        )
                    )
                )
            # Add the ray to its span.
            if ray_result.payload not in span.rays:
                span.rays.append(ray_result.payload)
                
        # --- Send the success result to the caller. ---#
        return ComputationResult.success(span)
