import { Body, Controller, Post } from '@nestjs/common';
import { NotifyService } from './notify.service';

@Controller('webhook')
export class WebhookController {
  constructor(private readonly notifyService: NotifyService) {}

  @Post('line')
  handle(@Body() payload: Record<string, unknown>) {
    return this.notifyService.handleLineEvent(payload);
  }
}
